from urllib import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
import os
import numpy as np
from PIL import Image

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        # id=request.POST.get('id')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phoneNumber=request.POST.get('phoneNumber')
        gen=request.POST.get('gen')
        adrs=request.POST.get('adrs')
        District=request.POST.get('District')
        regmodel(fname=fname,email=email,password=password,phoneNumber=phoneNumber,gen=gen,adrs=adrs,District=District).save()
        return redirect('login')
    else:
     return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def log(request):
    if request.method=="POST":
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        password=request.POST.get('password')

        cr=regmodel.objects.filter(fname=fname,password=password)
        if cr:
            user=regmodel.objects.get(fname=fname,password=password)
            id=user.id
            fname=user.fname
            password=user.password
            request.session['id']=id
            request.session['fname']=fname
            request.session['password']=password

            return redirect('home1')
        else:
         return render(request,'login.html')
    else:
        return render(request,'register.html')


def home1(request):
    return render(request,'home1.html')

def home(request):
    cr=orphanagemodel.objects.all()
    return render(request,'home.html',{'cr':cr})

def donation(request):
    if request.method=="POST":
        username=request.POST.get('username')
        Orphanagename=request.POST.get('Orphanagename')
        amount=request.POST.get('amount')
        donationmodel(username=username,Orphanagename=Orphanagename,amount=amount).save()
        return redirect('submit')
    else:
     return render(request,'donation.html')

def submit(request):
    return render(request,'submit.html')