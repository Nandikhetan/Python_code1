from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class StudentInfo(models.Model):

    Rollno=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=50)
    Class=models.CharField(max_length=50)
    School=models.CharField(max_length=100)
    mobile_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$')
    Mobile=models.CharField(validators=[mobile_regex],max_length=17,blank=True)
    Address=models.CharField(max_length=200)






    def __str__(self):
        return self.Name




class StudentAcademics(models.Model):
    Rollno=models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    Mathsmarks=models.IntegerField()
    Physicsmarks=models.IntegerField()
    Chemistrymarks=models.IntegerField()
    Biologymarks=models.IntegerField()
    Englishmarks=models.IntegerField()









# Create your models here.
