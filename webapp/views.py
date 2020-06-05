from django.shortcuts import render
from api.models import Student

# Create your views here.

def Index(request):
    # students = Student.objects.all()
    return render(request, 'webapp/index.html')
