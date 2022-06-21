import logging
import os

import click
import pandas as pd
import pandas.io.formats.excel

from rms.backend.conversions import Converter
from rms.backend.spreadsheet import Spreadsheet

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option('--spreadsheet-file', help="Path to the spreadsheet file")
@click.option('--skiprows', default=0, help="Number of top rows to skip")
@click.option('--skipfooter', default=0, help="Number of bottom rows to skip")
@click.option('--sheet-name', default=0, type=str, help="Excel sheet name")
@click.option('--columns-file', default='', help="Optional JSON file with columns mappings")
@click.option('--values-file', default='', help="Optional JSON file with values mappings")
@click.option('--mappers-file', default='', help="Optional JSON file with mappers description")
@click.option('--constants-file', default='', help="Optional JSON file with constant columns like"
                                                   "BLDGSCHEME or CNTRYSCHEME")
def main(spreadsheet_file, skiprows, skipfooter, sheet_name,
         columns_file, values_file, mappers_file, constants_file):
    base, _ = os.path.splitext(spreadsheet_file)
    if not columns_file:
        columns_file = base+'_columns.json'
    if not values_file:
        values_file = base+'_values.json'
    if not mappers_file:
        mappers_file = base+'_mappers.json'

    spreadsheet = Spreadsheet(spreadsheet_file)
    spreadsheet.load(sheet_name=sheet_name, skiprows=skiprows, skipfooter=skipfooter)

    converter = Converter()

    if not os.path.exists(columns_file):
        # Generate column mapping and STOP, need to verify these manually
        converter.generate_columns_mapping(spreadsheet, save_dir=columns_file)
        return

    converter.load_columns_mapping(columns_file)
    converter.load_mappers(mappers_file)

    if not os.path.exists(values_file):
        # Generate non-trivial mapping proposals and STOP, need to verify these manually
        converter.generate_values_mapping(spreadsheet, skip_trivial=True, save_dir=values_file)
        return

    converter.load_values_mapping(values_file)
    # Need to generate the values mapping again, since we saved only the non-trivial ones
    converter.generate_values_mapping(spreadsheet, skip_trivial=False)
    df = converter.convert_spreadsheet(spreadsheet)

    if constants_file:
        df = converter.add_constant_columns(df, constants_file)

    save_dir = base + '_processed.xlsx'
    df.to_excel(save_dir, sheet_name='RMS Data', index=False)
    writer = pd.ExcelWriter(save_dir, engine='xlsxwriter')
    pd.io.formats.excel.header_style = None
    df.to_excel(writer, sheet_name='RMS Data', index=False)
    workbook = writer.book
    worksheet = writer.sheets['RMS Data']
    # header = workbook.add_format()
    # header.set_font_color('red')
    worksheet.set_column(0, 220, 20)
    workbook.formats[0].set_font_size(8)
    # worksheet.set_row(0, None, header)
    writer.save()


if __name__ == "__main__":
    main()
