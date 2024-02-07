from django.db import models

# Create your models here.
class OpenRoom(models.Model):
    title = models.CharField(max_length=255)
    desc =  models.TextField()
    topic = models.CharField(max_length=255)
    link =  models.CharField(max_length=155)
    code = models.CharField(max_length=255)
 