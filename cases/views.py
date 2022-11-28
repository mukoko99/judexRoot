from unicodedata import name
from django.shortcuts import render
from .forms import *

def index(request):
   return render(request, 'base.html') 

def defendant_lookup(request):
    submitted = False
    if request.method == 'POST':
        form = DefendantForm(request.POST)
        if form.is_valid():
            defendant = Defendant.objects.filter(name = request.POST['name'])
            submitted = True
            return render(request, 'defendantLookup.html', {'form':form, 'submitted':submitted, 'defendant':defendant})
            
    else:
        form = DefendantForm()
        return render(request, 'defendantLookup.html', {'form':form, 'submitted':submitted})