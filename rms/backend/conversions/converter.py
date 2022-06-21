from __future__ import annotations

import simplejson as json
from collections import defaultdict
from typing import Dict

from rms.backend.constants import LOCATION_COLUMNS, BUILDING_COLUMNS, EQ_VAL_COLUMNS, EQ_SITE_COLUMNS, WS_VAL_COLUMNS, \
    WS_SITE_COLUMNS, TO_VAL_COLUMNS, TO_SITE_COLUMNS, FR_VAL_COLUMNS, FR_SITE_COLUMNS, TR_VAL_COLUMNS, TR_SITE_COLUMNS, \
    FL_VAL_COLUMNS, FL_SITE_COLUMNS, EQ_FEATURES, WS_FEATURES, TO_FEATURES, FL_FEATURES, FR_FEATURES
from rms.backend.conversions.mappers import *
from rms.backend.conversions.proposals import propose_column_mapping
from rms.backend.spreadsheet import Spreadsheet, Column

COLUMNS = LOCATION_COLUMNS + BUILDING_COLUMNS + EQ_VAL_COLUMNS + EQ_SITE_COLUMNS + WS_VAL_COLUMNS \
         + WS_SITE_COLUMNS + TO_VAL_COLUMNS + TO_SITE_COLUMNS + FR_VAL_COLUMNS + FR_SITE_COLUMNS + TR_VAL_COLUMNS\
         + TR_SITE_COLUMNS + FL_VAL_COLUMNS + FL_SITE_COLUMNS + EQ_FEATURES + WS_FEATURES + TO_FEATURES + FL_FEATURES\
         + FR_FEATURES


class Converter:
    """A class to convert the spreadsheet. Requires three mappings:

    i) Original column(s) to RMS column(s) mapping
    ii) Values mapping
    iii) RMS column to mapper mapping."""

    def __init__(self, columns_mapping: Dict = None, values_mapping: Dict = None,
                 mappers_mapping: Dict = None):
        self.columns = columns_mapping
        self.values = values_mapping
        self.rms_columns_mappers = mappers_mapping
        self.original_columns_mappers = None


    def load_mappers(self, json_path: str) -> Dict:
        """A method to load mapper objects from a file. The JSON structure must be
        {
        RMS_COLUMN_NAME: {"mapper": MAPPER_NAME, "kwargs": {kwargs dict to instantiate the mapper object}}
        }

        :param json_path: Path to JSON file with mappers description.
        :returns: If there is no self.columns attribute, returns a dict with keys being RMS column names.
          If there attribute is not None, it sets the original_columns_mappers attribute,
          mapping RMS column names in the dict to the original column names.
          original_columns_mappers is necessary to peform a successful conversion."""

        with open(json_path, 'r') as f:
            mappers = json.load(f)

        loaded_mappers = {}
        for k, v in mappers.items():
            logging.info(f"Loading mapper {v}")
            mapper_class = globals().get(v['mapper'])
            mapper_instance = mapper_class(**v['kwargs'])
            loaded_mappers[k] = mapper_instance

        self.rms_columns_mappers = loaded_mappers

        if self.columns is not None:
            self.original_columns_mappers = \
                {p: loaded_mappers.get(self.columns.get(p, None), None) for p in self.columns.keys()}

        return loaded_mappers


    def load_columns_mapping(self, columns_file: str):
        with open(columns_file, 'r') as f:
            proposals = json.load(f)
            # Group keys into tuples if they share values
            grouped = defaultdict(list)
            for key, item in proposals.items():
                grouped[item].append(key)
            proposals = {}

            for key, item in grouped.items():
                if len(item) == 1:
                    proposals[item[0]] = key
                else:
                    proposals[tuple(item)] = key

        self.columns = proposals
        return proposals


    def load_values_mapping(self, values_file: str):
        with open(values_file, 'r') as f:
            proposals = json.load(f)
            proposals = {k: dict(proposals[k]) for k in proposals.keys()}

        self.values = proposals
        return proposals


    @staticmethod
    def generate_columns_mapping(spreadsheet: Spreadsheet, save_dir: str = None) -> Dict:
        columns = spreadsheet.columns
        proposals = {}
        for col in columns:
            proposals.update(propose_column_mapping(col))
        if save_dir is not None:
            with open(save_dir, 'w') as f:
                json.dump(proposals, f, indent=2)
        return proposals


    def generate_values_mapping(self, spreadsheet: Spreadsheet, skip_trivial: bool = False,
                            save_dir: str = None) -> Dict:

        """Generates proposals for values mapping.

        :param spreadsheet: Spreadsheet
        :param skip_trivial: Flag deciding whether trivial mappings should be skipped from proposals
        :param save_dir: Directory to save the mapping

        :returns: Dumps a dict with proposed mappings of the form {original_column_name: List[Tuple]},
        where tuples encode proposed conversions. Done this way to be able to dump to json and then
        load and avoid casting problems int->str->str (ints can be Python dict keys but can't be
        JSON keys).

        Returns a Python dict, with List[Tuple] loaded into dicts."""

        mapping_proposal = {}
        for column_name in self.original_columns_mappers.keys():
            logging.info(f"Converting column {column_name}")
            mapper = self.original_columns_mappers[column_name]

            # Skip columns without mappers + no need to preserve proposals for copying or casting mappings.
            # Currently unable to save proposals for multicolumn mappings

            if mapper is None:
                continue

            if isinstance(mapper, (FloatMapper, IntMapper, CopyMapper, MultiColumnMapperMixin,
                                   YearBuiltMapper)) and skip_trivial:
                continue

            if isinstance(column_name, tuple):
                proposals = mapper.generate_proposals(*spreadsheet[column_name])
            else:
                proposals = mapper.generate_proposals(spreadsheet[column_name])

            mapping_proposal.update({column_name: proposals})

        if save_dir is not None:
            with open(save_dir, 'w') as f:
                json.dump(mapping_proposal, f, indent=1, ignore_nan=True)

        # Remap the mapping dict to actual Python dict of dicts
        mapping_proposal = {k: dict(mapping_proposal[k]) for k in mapping_proposal.keys()}

        # Merge with saved values mapping
        if self.values is not None:
            self.values = {**mapping_proposal, **self.values}

        return mapping_proposal


    def convert_spreadsheet(self, spreadsheet: Spreadsheet) -> pd.DataFrame:
        """Method converting the spreadsheet using a sequence of column mappings.
        A bit of spaghetti to handle cases if the argument/return of mapper
        is a tuple (many-to-many) or one element.

        :param spreadsheet: Spreadsheet to convert.
        :returns: The converted spreadsheet, obtained by applying a chain of mappings."""


        df = pd.DataFrame(columns=COLUMNS)
        for col, mapper in self.original_columns_mappers.items():
            try:
                if isinstance(col, tuple):
                    columns = tuple(Column(c, spreadsheet.df[c]) for c in col)
                    converted = mapper(*columns, mapping=self.values[col])
                    for c in converted:
                        df[c.name] = c.values

                else:
                    column = Column(col, spreadsheet.df[col])
                    converted = mapper(column, mapping=self.values[col])
                    if isinstance(mapper, MultiColumnMapperMixin):
                        for c in converted:
                            df[c.name] = c.values
                    else:
                        df[converted.name] = converted.values

            except Exception as e:
                logging.info(f'Unable to convert column {col}')

        return df


    @staticmethod
    def add_constant_columns(df: pd.DataFrame, columns_file: str) -> pd.DataFrame:
        with open(columns_file, 'r') as f:
            columns = json.load(f)
        for k in columns.keys():
            if k in COLUMNS:
                df[k] = columns[k]

        return df
