from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee
from .forms import EmployeeForm
from . import forms


# Create your views here.
def index(request):
    my_obj= Employee.objects.all()
    context={'my_obj':my_obj}
    return render(request, 'firstapp/index.html',context=context)

def formIndex(request):
    form=EmployeeForm()
    if request.method== "POST":
        form= forms.EmployeeForm(request.POST)
        if form.is_valid():
            # print('form is valid')
            # print('Name: ', form.cleaned_data['ename'])
            Employee.objects.create(ename= form.cleaned_data['ename'],eaddr= form.cleaned_data['eaddr'],enum= form.cleaned_data['enum'],esal= form.cleaned_data['esal'])
    context={'form':form}
    return render(request, 'firstapp/employee.html',context=context)
