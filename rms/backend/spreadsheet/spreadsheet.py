import logging
from collections import Counter
from typing import Iterable, Union, Tuple
from rms.backend.constants import BAD_VALUES

import pandas as pd
from rms.backend.conversions.types import ColumnType
from rms.backend.loaders import SpreadsheetLoader


class Spreadsheet:
    def __init__(self, spreadsheet_path: str):
        self.loader = SpreadsheetLoader(spreadsheet_path)
        self.df = pd.DataFrame()

    def __len__(self):
        return len(self.df)

    def __getitem__(self, item):
        return self._get_column(item)

    def _get_column(self, column_name: Union[str, Tuple]):
        if isinstance(column_name, str):
            return Column(column_name, self.df[column_name])
        return tuple(Column(cn, self.df[cn]) for cn in column_name)

    def get_columns(self):
        return [self._get_column(col) for col in self.columns]

    def load(self, **kwargs) -> pd.DataFrame:

        # def _should_prune_column(dataframe: pd.DataFrame, column_name:str):
        #     col = dataframe[column_name]
        #     values = set(col.value_counts().to_dict().keys())

        logging.info(f'Loading spreadsheet {self.loader.spreadsheet_path}')
        df = self.loader.load(**kwargs)
        df = df.dropna(how='all', axis=1)  # Drop empty columns, we will not need them
        df = df.dropna(how='all', axis=0)  # Drop empty rows, we will not need them
        df = df.fillna('')
        self.df = df
        return df

    def add_column(self, column_name: str, default_value=None):
        self.df[column_name] = default_value

    def get_column_types(self):
        return [pd.api.types.infer_dtype(self.df[c], skipna=True) for c in self.df.columns]

    @property
    def columns(self):
        return list(self.df.columns)


class Column:
    def __init__(self, column_name: str, column_values: Iterable):
        self.name = column_name
        self.values = pd.Series(column_values)
        self.dtype = ColumnType(pd.api.types.infer_dtype(self.values, skipna=True))

    def __getitem__(self, index):
        return self.values.iloc[index]

    def __len__(self):
        return len(self.values)

    def get_unique_values(self):
        return list(self.values.value_counts(dropna=False).to_dict().keys())
