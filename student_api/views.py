from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = StudentSerializer # tell django what serializer to use

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all().order_by('id')
    serializer_class = StudentSerializer