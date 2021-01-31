from django.db import models

# Create your models here.
class participant(models.Model):
    name = models.CharField(max_length=40)
    number = models.PositiveBigIntegerField()
    email = models.EmailField()
    rgType = models.CharField(max_length=10)
    NoPeople = models.PositiveIntegerField(default=1)  
    
      
