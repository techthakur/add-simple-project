from django.db import models

# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=50)
    college= models.CharField(max_length=50)
    rollnumber = models.CharField(max_length=15)
    phone = models.CharField(max_length=13)
    desc = models.TextField(max_length=500)
    date = models.DateField()


    
    def __str__(self):
        return self.name

