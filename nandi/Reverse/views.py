from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Person, Employee
from . Serializers import PersonSerializer,EmployeeSerializer

class PersonList(APIView):

    def get(self, request):
        Person1=Person.objects.all()
        serializer=PersonSerializer(Person1, many=True)
        return Response(serializer.data)


    def post(self, request):
        Employee1=Employee.objects.all()
        serializer=EmployeeSerializer(Employee1, many=True)
        return Response(serializer.data)




def Employeee(request):
    return HttpResponse("<h1> HOME</h1>")

# Create your views here.
