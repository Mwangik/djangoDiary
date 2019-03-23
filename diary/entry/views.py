from django.shortcuts import render
from . import templates

def index(request):
    return render(request, 'entry/index.html')

def add(request):
    return render(request, 'entry/add.html')
