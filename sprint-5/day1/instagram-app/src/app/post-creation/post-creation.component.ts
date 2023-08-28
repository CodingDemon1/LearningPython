import { Component } from '@angular/core';
import { PostService } from '../post.service';


@Component({
  selector: 'app-post-creation',
  templateUrl: './post-creation.component.html',
  styleUrls: ['./post-creation.component.css']
})
export class PostCreationComponent {
  username: string = '';
  caption : string = '';

  constructor(private postService: PostService){}

  createPost():void{
    const newPost = {
      username: this.username,
      caption : this.caption,
      likes: 0,
      comments: []
    }

    this.postService.addPost(newPost)

    this.username = ''
    this.caption = ''
  }
}
