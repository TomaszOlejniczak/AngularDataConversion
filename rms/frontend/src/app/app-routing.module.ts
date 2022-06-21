import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ImportComponent } from './pages/import/import.component';
import { HelpComponent } from './pages/help/help.component';
import { ResultComponent } from './pages/result/result.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/importer',
    pathMatch: 'full',
  },
  { path: 'importer', component: ImportComponent },
  { path: 'help', component: HelpComponent },
  { path: 'result', component: ResultComponent },
  // { path: 'confirm', component: ConfirmComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
