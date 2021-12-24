from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=80)

class Employee(models.Model):
    Employeeid=models.IntegerField()
    department=models.CharField(max_length=100)
    role=models.CharField(max_length=100)





# Create your models here.
