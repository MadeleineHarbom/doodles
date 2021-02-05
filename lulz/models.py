from django.db import models

# Create your models here.

class Comment(models.Model):
    #inherit to make objects
    text = models.TextField()
    comic_id = models.CharField(max_length=50)
    user = models.CharField(max_length=20)
    #defines some field on Model
