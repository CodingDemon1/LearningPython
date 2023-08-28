import { PostService } from './../post.service';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-display',
  templateUrl: './post-display.component.html',
  styleUrls: ['./post-display.component.css']
})
export class PostDisplayComponent implements OnInit {
  posts:any[] = []
  // @Input() posts:any[]=[]
  constructor(private postService: PostService){}

  deletePost(index:number){
    this.posts.splice(index,1)
  }

  ngOnInit(){
    this.posts = this.postService.getPosts()
  }
  
}

