#import csv
#from django.http import HttpResponse
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class ViewList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    '''
    def get_csv(self):

        queryset = Employee.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        serializer = EmployeeSerializer(queryset, many=True)

        header = EmployeeSerializer.Meta.fields

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)

        return response
    '''
