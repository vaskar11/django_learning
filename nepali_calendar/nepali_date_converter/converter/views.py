from django.shortcuts import render
from django.http import HttpResponse
from .logic import calculate_nepali_date

# Create your views here.

def index(request):
    return render(request,'converter/index.html')

def convert_date(request):
    if request.method =="POST":
        year= int(request.POST['year'])
        month= int(request.POST['day'])
        day= int(request.POST['day'])
        
        nepali_date, weekday, tithi, event, calendar= calculate_nepali_date(year, month,day)
        
        context={
            'nepali_date': nepali_date,
            'weekday':weekday,
            'tithi': tithi,
            'event':event,
            'calendar': calendar
        }

        return render(request, 'converter/result.html', context=context)
    
    