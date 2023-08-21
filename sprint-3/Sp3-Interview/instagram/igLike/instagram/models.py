from django.db import models

# Create your models here.


class Post(models.Model):
    username = models.CharField(max_length=100)
    caption = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)
