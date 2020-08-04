from django import forms
from django.contrib.auth.models import User
from base_app.models import Adder

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model=Adder
        fields=('portfolio_site','user_pic')
