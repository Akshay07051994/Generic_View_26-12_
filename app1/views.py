from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class StudentAPI(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()