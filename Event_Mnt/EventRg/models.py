from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    fromDt = models.DateTimeField()
    toDt = models.DateTimeField()
    deadline = models.DateTimeField()
    mail = models.EmailField()
    pwd = models.TextField(max_length=10)