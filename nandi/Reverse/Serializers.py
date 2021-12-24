from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from . models import Person, Employee



class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields=('name','age','email')
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        feilds=('Employeeid','department','role')
        fields='__all__'
