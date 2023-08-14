from django.shortcuts import render
from .models import Post


# Create your views here.
def ViewPost(req):
    if req.method == "POST":
        userName = req.POST.get("userName")
        caption = req.POST.get("caption")

        if userName and caption:
            post = Post(userName=userName, caption=caption)
            post.save()

    return render(req, "create_post.html")


def delPost(req, post_id):
    post = post.objects.get(id=post_id)
    post.delete()
