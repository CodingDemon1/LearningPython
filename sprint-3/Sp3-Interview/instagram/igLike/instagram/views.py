from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post
import json

# Create your views here.


def show_post(req):
    if req.method == "GET":
        posts = Post.objects.all()
        post_data = []

        for post in posts:
            post_data.append(
                {"id": post.id, "username": post.username, "caption": post.caption}
            )
            return JsonResponse({"post": post_data})


def delete_post(req, pID):
    if req.method == "DELETE":
        posts = Post.objects.all()
        for post in posts:
            if post.id == pID:
                post.delete()
                return JsonResponse({"msg": "Post Deleted"})


def create_post(req):
    if req.method == "POST":
        newPost = json.loads(req.body)

        post = Post(username=newPost["username"], caption=newPost["caption"])
        post.save()

        return JsonResponse({"msg": "Post created"})
