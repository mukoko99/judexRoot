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
            defendant = Defendant.objects.filter(firstName = request.POST['firstName'], gender = request.POST['gender'])
            submitted = True
            return render(request, 'defendantLookup.html', {'form':form, 'submitted':submitted, 'defendant':defendant})
            
    else:
        form = DefendantForm()
        return render(request, 'defendantLookup.html', {'form':form, 'submitted':submitted})

def case_lookup(request):
    submitted = False
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            defendantVal = Defendant.objects.get(id=request.POST['defendant'])
            judgeVal = Judge.objects.get(id = request.POST['judge'])
            result = Case.objects.filter(judge = judgeVal, defendant = defendantVal)
            submitted = True
            return render(request, 'caseLookup.html', {'result': result, 'form': form, 'submitted': submitted})
    else:
        form = CaseForm()
        return render(request, 'caseLookup.html', {'form':form, 'submitted': submitted})