from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Doctor,Appointment
from django.core.validators import RegexValidator

# Register Form
class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields = ['username','email']
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }
        
# Login Form
class AdminSiginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
# Appointment Form
class AppointmentForm(forms.ModelForm):

    class Meta:
        model=Appointment
        fields=["Name","phone","Email","address","place","Date","time_slot","doctor_Name"]
        widgets={
            "Name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "Email":forms.EmailInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "Date":forms.DateInput(attrs={'type': 'date'}),
            "time_slot":forms.TimeInput(attrs={'type': 'time'}),
        }

# New Doctor
class DoctorForm(forms.ModelForm):  
    class Meta:
        model=Doctor
        fields="__all__"

