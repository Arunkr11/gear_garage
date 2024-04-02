from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from store.models import Vehicle


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class BikeAddingForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=["title","image","decription","brand_object","category","fuel","kms","location","owner_type","price"]


