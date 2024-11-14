from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee

# Create your views here.

def index(request):
    emp_list= Employee.objects.all()
    context= {'emp_list':emp_list}
    return render(request,'firstapp/index.html', context=context)
