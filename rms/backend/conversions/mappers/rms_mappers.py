"""Classes responsible for mapping to RMS columns.

Each such class needs to implement the _convert_value() method."""

import logging
import re
from datetime import datetime
from typing import Tuple

import dateparser
import numpy as np
import pandas as pd
import pycountry
from fuzzywuzzy import fuzz, process

from rms.backend.constants import COUNTRY_CODES_ISO2, COUNTRY_CODES_ISO3, ISO3_TO_ISO2
from rms.backend.conversions.mappers import BaseRMSMapper, MultiColumnMapperMixin
from rms.backend.conversions.types import ColumnType
from rms.backend.conversions.utils import prune_zip4


class YearBuiltMapper(BaseRMSMapper):
    def __init__(self, target_column='YEARBUILT', target_type=ColumnType.STRING):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> str:
        if not isinstance(value, str):
            value = str(value)
        try:
            year = dateparser.parse(value).year
            return '1/1/' + str(year)
        except AttributeError:
            match = re.compile(r'\d{4}').match(value)
            if match:
                year = match.group()
                return '1/1/' + year
        return ''  # Also for values like ' ' or 'Unknown'


class RoofAgeMapper(BaseRMSMapper):
    def __init__(self, target_column='ROOFAGE', target_type=ColumnType.INT):
        super().__init__(target_column, target_type)

    def _convert_value(self, value):
        if not isinstance(value, str):
            value = str(value)
        try:
            year = dateparser.parse(value).year
        except AttributeError:
            match = re.compile(r'\d{4}').match(value)
            if match:
                year = int(match.group())
            else:
                return 0

        # Check if it's absolute age or year value
        if year > 100:
            roof_age = datetime.now().year - year
        else:
            roof_age = year

        if roof_age <= 5:
            return 1
        if 5 < roof_age <= 10:
            return 2
        if 11 < roof_age:
            return 3


class ZipCodeMapper(BaseRMSMapper):
    def __init__(self, target_column='POSTALCODE', target_type=ColumnType.STRING, country=None):
        self.country = country
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> str:
        """
        Need to deal with some cases, including loading ints as floats if there are NaNs
        present in the column or ZIP4 codes in the USA.

        :param value: Postal code as float/string/int
        :return: String with postal code, parsed for USA and simply copied for other countries
        """

        try:
            if not isinstance(value, str):  # Float or int, float should be castable to int
                value = int(value)
                value = str(value)
            if self.country == 'USA':
                return prune_zip4(value)
            return value
        except ValueError:
            return ''


class NumStoriesMapper(BaseRMSMapper):
    def __init__(self, target_column='NUMSTORIES', target_type=ColumnType.INT):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> int:
        try:
            val = float(value)
            if not np.isnan(val):
                return int(np.ceil(val))
            return 0
        except ValueError:
            value = str(value)

        predicates_precedence = [re.compile(r'\d{2}'), re.compile(r'\d')]  # match 2-digit, then 1 digit bldgs

        for p in predicates_precedence:
            match = p.findall(value)
            if match:
                return max((int(m) for m in match))

        return 0


class FireAlarmMapper(BaseRMSMapper):
    def __init__(self, target_column='FRFIREALARM', target_type=ColumnType.INT):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> int:
        if str(value) not in self.values.keys():
            proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
            best = self.values.get(proposals[0][0])
            return best

        return self.values.get(str(value))


class EngineeredFoundationsMapper(BaseRMSMapper):
    def __init__(self, target_column='ENGFOUND', target_type=ColumnType.INT):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> int:
        if str(value) not in self.values.keys():
            proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
            best = self.values.get(proposals[0][0])
            return best

        return self.values.get(str(value))


class ConstructionClassMapper(BaseRMSMapper):
    def __init__(self, target_column='BLDGCLASS', target_type=ColumnType.STRING):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> int:
        if str(value) not in self.values.keys():
            proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
            best = self.values.get(proposals[0][0])
            return best

        return self.values.get(str(value))


class SprinklerMapper(BaseRMSMapper):
    def __init__(self, target_column='FRSPRINKLERSYS', target_type=ColumnType.INT):
        super().__init__(target_column, target_type)

    def _convert_value(self, value):
        # TODO: Why return 2 if negative sprinklers?
        try:
            val = float(value)
            if np.isnan(val) or val == 0:
                return 0
            if val > 0:
                return 1
        except (ValueError, TypeError):
            if str(value) not in self.values.keys():
                proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
                best = self.values.get(proposals[0][0])
                return best

            return self.values.get(str(value))


class CountryMapper(BaseRMSMapper):
    def __init__(self, target_column='CNTRYCODE', target_type=ColumnType.STRING):
        super().__init__(target_column, target_type)

    def _convert_value(self, value):
        if not value == '':
            if value in COUNTRY_CODES_ISO2:
                return value
            if value in COUNTRY_CODES_ISO3:
                return ISO3_TO_ISO2.get(value)
            try:
                countrycode = pycountry.countries.get(name=value.lower().capitalize()).alpha_2
                return countrycode
            except:
                logging.info(f'Couldn"t convert country name {value}')
                return ''
        return ''


class USAStateMapper(BaseRMSMapper):
    def __init__(self, target_column='STATECODE', target_type=ColumnType.STRING):
        super().__init__(target_column, target_type)

    def _convert_value(self, value):
        value = value.strip()
        if value in self.values.values():
            return value

        proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
        best = self.values.get(proposals[0][0])
        return best


class BuildingValueMapper(MultiColumnMapperMixin):
    def __init__(self, target_columns=('EQCV1VAL', 'FRCV1VAL', 'FLCV1VAL', 'TOCV1VAL', 'TRCV1VAL', 'WSCV1VAL')):
        super().__init__(target_columns)

    def _convert_values(self, values: pd.Series) -> pd.Series:
        """Only one value, building replacement cost"""
        val = values[0]

        # Make sure that the keys of the returned dict are exactly the same as
        # target columns (maybe a subset would work as well)
        return pd.Series({k: val for k in self.target_columns})


class ContentsValueMapper(MultiColumnMapperMixin):
    def __init__(self, target_columns=('EQCV2VAL', 'FRCV2VAL', 'FLCV2VAL', 'TOCV2VAL', 'TRCV2VAL', 'WSCV2VAL')):
        super().__init__(target_columns)

    def _convert_values(self, values: pd.Series) -> pd.Series:
        """Only one value, contents replacement cost"""
        val = values[0]

        # Make sure that the keys of the returned dict are exactly the same as
        # target columns (maybe a subset would work as well)
        return pd.Series({k: val for k in self.target_columns})


class BIValueMapper(MultiColumnMapperMixin):
    def __init__(self, target_columns=('EQCV3VAL', 'FRCV3VAL', 'FLCV3VAL', 'TOCV3VAL', 'TRCV3VAL', 'WSCV3AL')):
        super().__init__(target_columns)

    def _convert_values(self, values: pd.Series) -> pd.Series:
        """Only BI value"""
        val = values[0]

        # Make sure that the keys of the returned dict are exactly the same as
        # target columns (maybe a subset would work as well)
        return pd.Series({k: val for k in self.target_columns})


class ValueMapper(MultiColumnMapperMixin):
    def __init__(self, target_columns=None):
        super().__init__(target_columns)

    def _convert_values(self, values: Tuple) -> pd.Series:
        try:
            val = int(values[0])
        except ValueError:
            val = 0

        # Make sure that the keys of the returned dict are exactly the same as
        # target columns (maybe a subset would work as well)
        return pd.Series({k: val for k in self.target_columns})
