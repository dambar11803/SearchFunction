from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    name= models.CharField(max_length=200)
    address= models.CharField(max_length=150)
    phone= models.CharField(max_length=15)
    roll= models.CharField(max_length=10)
    level= models.CharField(max_length=10)
    subject= models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    


