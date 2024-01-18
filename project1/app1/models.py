from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 40)
    rollno = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    section = models.CharField(max_length=60)
    
