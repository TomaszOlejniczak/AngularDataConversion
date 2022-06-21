export interface DataTable {
  columns: Array<string>;
  rows: Array<DataRow>;
  rmsColumns: Array<string>;
  rmsProposal: RmsProposal;
  fileName: string;
}

export interface DataRow {
  [key: string]: string | number;
}

export interface RmsProposal {
  [key: string]: string;
}
