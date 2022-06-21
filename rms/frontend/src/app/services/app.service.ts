import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpService } from './http.service';
import { BehaviorSubject, Observable } from 'rxjs';
import {
  ConvertedSpreadsheet,
  Spreadsheet,
} from '../models/converted-spreadsheet.model';
import { DataTable, DataRow } from '../models/data-table.model';
import { ProcessValues } from '../models/process-values';

@Injectable({
  providedIn: 'root',
})
export class AppService {
  private dataTable = new BehaviorSubject<DataTable>(null);
  private response = new BehaviorSubject<any>(null);
  constructor(private router: Router, private httpService: HttpService) {}

  getDataTable(): Observable<DataTable> {
    return this.dataTable.asObservable();
  }

  process(file, rowsNum, footNum): void {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    formData.append(
      'read_params',
      `{"skiprows": ${rowsNum}, "skip_footer": ${footNum}}`
    );
    this.httpService
      .processSpreadsheet(formData)
      .subscribe((data: ConvertedSpreadsheet) => {
        const dataTable = this.createDataTableStructure(data);
        dataTable.fileName = file.name;
        this.dataTable.next(dataTable);
      });
    this.router.navigateByUrl('/result');
  }

  processValues(values: ProcessValues): void {
    this.httpService.processValues(values).subscribe((response: any) => {
      this.response.next(response);
      console.log(response);
    });
    // this.router.navigateByUrl('/confirm');
  }

  private createDataTableStructure(data: ConvertedSpreadsheet): DataTable {
    const columns = Object.keys(data.spreadsheet);
    const spreadsheet = data.spreadsheet;
    const amountOfRows = this.countRows(spreadsheet);
    const dataRows = new Array<DataRow>(amountOfRows);
    const rmsColumns = data.rms_columns;
    const rmsProposal = data.column_conversions;

    Object.entries(spreadsheet).forEach(([_, rows], index) => {
      const values = Object.values(rows);
      values.forEach((value, i) => {
        const cell: DataRow = { [columns[index]]: value };
        dataRows[i] = { ...dataRows[i], ...cell };
      });
    });
    return { columns, rows: dataRows, rmsColumns, rmsProposal } as DataTable;
  }

  private countRows(object: Spreadsheet): number {
    const amountOfRows = Object.entries(object)[0][1];
    return Object.keys(amountOfRows).length;
  }
}
