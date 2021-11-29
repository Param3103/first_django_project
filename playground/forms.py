from django import forms
from .models import Item
import time
class LoginForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Please enter your name: ")
    age = forms.CharField(help_text="Please enter your age: ")
    print(name,age)