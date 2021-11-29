from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Please enter your name: ")
    age = forms.IntegerField(min_value=1, help_text="Please enter your age: ")
