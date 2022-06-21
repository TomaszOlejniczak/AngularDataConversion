import { ProcessValues } from './../models/process-values';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ConvertedSpreadsheet } from '../models/converted-spreadsheet.model';

@Injectable({
  providedIn: 'root',
})
export class HttpService {
  constructor(private http: HttpClient) {}

  processSpreadsheet(formData: FormData): Observable<ConvertedSpreadsheet> {
    return this.http.post<ConvertedSpreadsheet>(
      'http://localhost:5000/api/process_spreadsheet',
      formData
    );
  }

  processValues(values: ProcessValues): Observable<any> {
    return this.http.post<ProcessValues>(
      'http://localhost:5000/api/process_values',
      values
    );
  }
}
