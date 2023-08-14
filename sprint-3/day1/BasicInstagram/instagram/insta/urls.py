from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreatePost, name="create"),
    path("view/", views.ViewPost, name="view"),
    path("delete/", views.delPost, name="Delete"),
]
