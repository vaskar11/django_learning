from django import forms

class UniversityForm(forms.Form):
    Subject_choice=(
        (1,"Web Dev"),
        (2,"System Programming"),
        (3,"Data Science"),
    )
    
    name= forms.CharField()
    age= forms.IntegerField()
    subject= forms.ChoiceField(choices=Subject_choice)
    date_of_birth= forms.DateField()
    