from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from app1.forms import StudentForm
from  app1.models import Student
from .forms import *
from .models import *



# Create your views here.

def showlinks(request):
    return render(request,"welcome.html")

def showform(request):
    form = StudentForm()
    return render(request,"index.html",{"form" :form})

def create(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:        
        form = StudentForm()
    return render(request,"index.html",{"form" :form})

def read(request):
    data = Student.objects.all()
    return render(request,"read.html",{'data':data})
    