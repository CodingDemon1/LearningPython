import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PostDisplayComponent } from './post-display/post-display.component';
import { PostCreationComponent } from './post-creation/post-creation.component';

const routes: Routes = [
  {path:"", component:PostDisplayComponent},
  {path:"create", component:PostCreationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
