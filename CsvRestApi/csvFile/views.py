#import csv
#from django.http import HttpResponse
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class ViewList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
