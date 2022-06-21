export interface ConvertedSpreadsheet {
  spreadsheet: Spreadsheet;
  column_conversions: ColumnConversion;
  rms_columns: Array<string>;
}

export interface Spreadsheet {
  [key: string]: { [key: string]: string | number };
}

export interface ColumnConversion {
  [key: string]: string;
}
