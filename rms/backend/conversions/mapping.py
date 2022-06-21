from typing import Dict, List, Callable

from rms.backend.spreadsheet import Spreadsheet


class ColumnMapping:
    def __init__(self, input_columns: List[str], output_columns: List[str], values_mapper: Callable):
        self.input_columns = input_columns
        self.output_columns = output_columns
        self.conversion = values_mapper

    def __call__(self, spreadsheet: Spreadsheet):
        pass

    @classmethod
    def mapping_from_dict(cls, data: Dict):
        """Method loading a ColumnMapping object from a dict with params."""
        pass
