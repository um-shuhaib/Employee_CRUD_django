# django forms - normal form and modelform

from django import forms
from employee.models import Employee
# normal forms 
# for styling need - widger-tweaks file 

class EmployeeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'c form-control ','placeholder':'name'}))
    salery=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'salary'}))
    designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'designation'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}))


# model form 

class ModelemployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # exclude=['phone']  
        # fields=["name","salery"]
        
        # for styling 
        widgets={
            "name":forms.TextInput(attrs={'class':'c form-control ','placeholder':'name'}),
            "salery":forms.NumberInput(attrs={'class':'c form-control ','placeholder':'name'}),
            "designation":forms.TextInput(attrs={'class':'c form-control ','placeholder':'name'}),
            "email":forms.EmailInput(attrs={'class':'c form-control ','placeholder':'name'}),
            "phone":forms.TextInput(attrs={'class':'c form-control ','placeholder':'name'})
        }