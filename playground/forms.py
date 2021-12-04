from django import forms
from .models import Item,File_URL
import time
class LoginForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "age"]
class URLForm(forms.ModelForm):
    class Meta:
        model = File_URL
        fields = ["path"]