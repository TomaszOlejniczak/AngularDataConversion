import { ConvertedSpreadsheet } from './../../models/converted-spreadsheet.model';
import {
  Component,
  OnInit,
  EventEmitter,
  Output,
  OnDestroy,
  Input,
} from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.scss'],
})
export class FileUploadComponent implements OnInit, OnDestroy {
  private file: File;
  fileControl: FormControl;
  fileInfo: FileInfo;
  rowsNum = 0;
  footNum = 0;
  @Output() fileSelected = new EventEmitter();

  private subscription: Subscription = new Subscription();

  constructor() {
    this.fileControl = new FormControl(null, [Validators.required]);
  }

  ngOnInit(): void {
    const sub = this.fileControl.valueChanges.subscribe((file: File) => {
      this.fileInfo = {
        name: file.name,
        size: file.size / 1024,
      };
      this.file = file;
    });
    this.subscription.add(sub);
  }

  onSend() {
    this.fileSelected.emit({
      file: this.file,
      rowsNum: this.rowsNum,
      footNum: this.footNum,
    });
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}

interface FileInfo {
  name: string;
  size: number;
}
