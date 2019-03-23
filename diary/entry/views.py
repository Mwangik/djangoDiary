from django.shortcuts import render

from .models import Entry

def index(request):
    entries = Entry.objects.order_by('-id')
    context = {
        'entries':entries,
    }
    return render(request, 'entry/index.html',context)

def add(request):
    return render(request, 'entry/add.html')
