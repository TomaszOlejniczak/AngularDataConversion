import logging

import numpy as np
from fuzzywuzzy import process, fuzz

from rms.backend.conversions.mappers import MapperMixin, BaseRMSMapper
from rms.backend.conversions.types import ColumnType


class CopyMapper(MapperMixin):
    """A trivial mapper which simply copies the values."""
    def __init__(self, target_column: str):
        super().__init__(target_column)

    def _convert_value(self, value):
        try:
            if np.isnan(value):
                return ''
            return value
        except TypeError:
            return value


class IntMapper(MapperMixin):
    def __init__(self, target_column: str, empty_value=None):
        self.empty_value = empty_value
        super().__init__(target_column)

    def _convert_value(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            logging.info(f'IntMapper unable to convert value {value}')
            return self.empty_value


class FloatMapper(MapperMixin):
    def __init__(self, target_column: str, empty_value=None):
        self.empty_value = empty_value
        super().__init__(target_column)

    def _convert_value(self, value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return self.empty_value


class StringMatchingMapper(BaseRMSMapper):
    def __init__(self, target_column='', target_type=ColumnType.STRING):
        super().__init__(target_column, target_type)

    def _convert_value(self, value) -> int:
        if str(value) not in self.values.keys():
            proposals = process.extract(str(value), list(self.values.keys()), scorer=fuzz.ratio)
            best = self.values.get(proposals[0][0])
            # TODO: Log when good proposal not found
            return best

        return self.values.get(str(value))
