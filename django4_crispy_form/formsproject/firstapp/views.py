from django.shortcuts import render
from django.http import HttpResponse

from .forms import UniversityForm



# Create your views here.
def index(request):

    context={'form':UniversityForm()}
    return render(request, 'firstapp/index.html',context=context)


