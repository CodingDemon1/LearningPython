import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class MenuService {
  private apiUrl = 'https://www.themealdb.com/api/json/v1/1/search.php?s=';
  constructor(private http: HttpClient) { }

  getDishes(searchTerm : string):Observable<any>{
    return this.http.get(`${this.apiUrl}${searchTerm}`)
  }

  getFilteredDishes(searchTerm: string): Observable<any> {
  return this.http.get(`${this.apiUrl}${searchTerm}`);
}
}
