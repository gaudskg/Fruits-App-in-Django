from curses.ascii import HT
from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request,'home.html')

def home_page(request):
    return HttpResponse("<h1>THIS IS HOME TAB</h1>")

def fruits_list(request):
    #fruits = ['apple','mango','banana','orange','strawberry','cherry']
    context = {'fruits' : fruits.objects.all()}
    return render(request,'home.html',context)