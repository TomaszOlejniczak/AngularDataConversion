import {
  Component,
  OnInit,
  ViewChild,
  EventEmitter,
  Output,
} from '@angular/core';
import { AppService } from 'src/app/services/app.service';
import { DataTable, DataRow } from 'src/app/models/data-table.model';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { Observable } from 'rxjs';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.scss'],
})
export class ResultComponent implements OnInit {
  dataTable: DataTable;
  dataSource: MatTableDataSource<DataRow>;
  private controlMap = new Map<string, FormControl>();
  private filteredOptionsMap = new Map<string, Observable<string[]>>();

  @Output() colsSelected = new EventEmitter();
  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;

  constructor(private appService: AppService) {}

  ngOnInit(): void {
    this.appService.getDataTable().subscribe((data: DataTable) => {
      if (data) {
        this.prepareAutocompleteFields(data);
        this.dataTable = data;
        this.dataSource = new MatTableDataSource<DataRow>(data.rows);
        this.dataSource.paginator = this.paginator;
      }
    });
  }

  onSelect(propsalValue: string, oldValue: string): void {
    this.dataTable.rmsProposal[oldValue] = propsalValue;
    console.log(this.dataTable.rmsProposal);
  }

  removeCol(col) {
    const index = this.dataTable.columns.indexOf(col, 0);
    if (index > -1) {
      this.dataTable.columns.splice(index, 1);
    }
    delete this.dataTable.rmsProposal[col];
    console.log(this.dataTable.rmsProposal);
  }

  getControl(columnName: string): FormControl {
    return this.controlMap.get(columnName);
  }

  getFilteredOptions(columnName: string): Observable<string[]> {
    return this.filteredOptionsMap.get(columnName);
  }

  acceptCols() {
    const processValues = {
      file_name: this.dataTable.fileName,
      converted_columns: this.dataTable.rmsProposal,
    };
    console.log(processValues);
  }

  private prepareAutocompleteFields(data: DataTable) {
    data.columns.forEach((columnName) => {
      this.controlMap.set(
        columnName,
        new FormControl(data.rmsProposal[columnName])
      );

      const filtered = this.controlMap.get(columnName).valueChanges.pipe(
        startWith(''),
        map((value) => this._filter(value))
      );
      this.filteredOptionsMap.set(columnName, filtered);
    });
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.dataTable?.rmsColumns.filter((option) =>
      option.toLowerCase().includes(filterValue)
    );
  }
}
