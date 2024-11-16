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
            form.save(commit=True)

        form = forms.EmployeeForm()
    context={'form':form}
    return render(request, 'firstapp/employee.html',context=context)
