from enum import Enum

class ColumnType(Enum):
    STRING = 'string'
    BYTES = 'bytes'
    INT = 'integer'
    FLOAT = 'floating'
    MIXED_INT = 'mixed-integer'
    MIXED_INT_FLOAT = 'mixed-integer-float'
    DECIMAL = 'decimal'
    COMPLEX = 'complex'
    CATEGORICAL = 'categorical'
    BOOL = 'boolean'
    DATETIME64 = 'datetime64'
    DATETIME = 'datetime'
    DATE = 'date'
    TIMEDELTA64 = 'timedelta64'
    TIMEDELTA = 'timedelta'
    TIME = 'time'
    PERIOD = 'period'
    MIXED = 'mixed'
