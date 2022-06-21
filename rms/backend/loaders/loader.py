import pandas as pd


class SpreadsheetLoader:
    def __init__(self, spreadsheet_path: str):
        self.spreadsheet_path = spreadsheet_path

    def load(self, **kwargs) -> pd.DataFrame:
        path = self.spreadsheet_path
        if path.endswith('csv'):
            df = pd.read_csv(path, **kwargs)
        elif path.endswith(('xls', 'xlsx', 'XLSX', 'XLS', 'xlsm', 'XLSM')):
            df = pd.read_excel(path, **kwargs)
        else:
            df = None

        # if df is not None:
        #     df.columns = df.columns.map(lambda x: x.replace('\r', '').replace('\n', ''))
        #     df.replace({r"\\t|\\n|\\r": " ", "\t|\n|\r": " "}, regex=True, inplace=True)

        return df
