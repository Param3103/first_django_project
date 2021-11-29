from django import forms
from .models import Item
import time
class LoginForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "age"]