from django.shortcuts import render
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer

# Create your views here.

@api_view(['GET'])
def apiMain(request):
    api_urls = {
        'List': 'student-list',
        'Detail View': '/student-detail/<str:pk>',
        'Create': '/student-create/',
        'Update': '/student-update/<str:pk>',
        'Delete': '/student-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def studentList(request):
    students = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentDetail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    students = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)