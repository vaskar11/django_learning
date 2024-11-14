from django import forms

class EmployeeForm(forms.Form):
    ename= forms.CharField(max_length=50)
    eaddr= forms.CharField(max_length=50)
    enum= forms.IntegerField()
    esal= forms.FloatField()