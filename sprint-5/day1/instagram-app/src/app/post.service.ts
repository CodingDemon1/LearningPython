import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PostService {
   private posts: any[]=[]
   addPost(post:any){
    this.posts.push(post)
   }

   getPosts(){
    return this.posts
   }

   deletePost(index:number){
    this.posts.splice(index,1)
   }
  constructor() { }
}
