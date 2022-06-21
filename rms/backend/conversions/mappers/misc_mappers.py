import re
import pandas as pd
from rms.backend.conversions.mappers import MapperMixin, MultiColumnMapperMixin


class ExtractIntMapper(MapperMixin):
    def __init__(self, target_column=''):
        super().__init__(target_column)

    def _convert_value(self, value) -> int:
        if not isinstance(value, str):
            value = str(value)
        match = re.compile(r'\d{1,10}').findall(value)
        if match:
            return int(match[-1])

        return 0


class AddColumnsMapper(MultiColumnMapperMixin):
    def __init__(self, target_columns=None):
        super().__init__(target_columns)

    def _convert_values(self, values) -> pd.Series:

        val_sum = 0
        # Try to add elements, skip to next if not possible
        for v in values:
            try:
                val_sum += v
            except (ValueError, TypeError):
                continue

        return pd.Series({k: val_sum for k in self.target_columns})
