from new.calc.models import Student
from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Student

# Create your views here.
def home(request):
    dest = Student.objects.all()
    return render(request, 'index.html');