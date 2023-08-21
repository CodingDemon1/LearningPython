from django.urls import path
from .views import show_post, create_post, delete_post

urlpatterns = [
    path("create/", create_post),
    path("", show_post),
    path("del/<int:pID>", delete_post),
]
