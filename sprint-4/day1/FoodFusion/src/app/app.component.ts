import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'FoodFusion';

   dishes : any[]=[];

  constructor(private menuService: MenuService){}
  filterTerm = '';

  applyFilter(): void {
    this.menuService.getFilteredDishes(this.filterTerm).subscribe(data => {
      this.dishes = data.meals || [];
    });
}
  ngOnInit():void{
    this.menuService.getDishes('').subscribe(data=>{
      this.dishes = data.meals || []
    })
  }
}



import { MenuService } from './menu.service';


export class MenuDisplayComponent {
 
}
