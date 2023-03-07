from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.

def index(request):
    abc=Students.objects.all()
    return render(request,'home.html',{'students':abc})