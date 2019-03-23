from django.shortcuts import render,redirect

from .forms import EntryForm
from .models import Entry

def index(request):
    entries = Entry.objects.order_by('-id')
    context = {
        'entries':entries,
    }
    return render(request, 'entry/index.html',context)

def add(request):
    if request.method=='POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()

    context={
        'form':form
    }

    return render(request, 'entry/add.html',context)
