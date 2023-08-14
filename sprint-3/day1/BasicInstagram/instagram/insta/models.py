from django.db import models


# Create your models here.
class Post(models.Model):
    userName = models.CharField(max_length=30)
    caption = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
