import { Component } from '@angular/core';
import { AppService } from 'src/app/services/app.service';

@Component({
  selector: 'app-import',
  templateUrl: './import.component.html',
  styleUrls: ['./import.component.scss'],
})
export class ImportComponent {
  constructor(private appService: AppService) {}

  onFileSelected(data: any) {
    this.appService.process(data.file, data.rowsNum, data.footNum);
  }
}
