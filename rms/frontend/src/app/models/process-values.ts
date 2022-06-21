export interface ProcessValues {
  file_name: string;
  converted_columns: AcceptedCols;
}

export interface AcceptedCols {
  [key: string]: string;
}
