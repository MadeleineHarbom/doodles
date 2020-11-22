from django.db import models

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    comic_id = models.CharField(max_length=50)
    user = models.CharField(max_length=20)
