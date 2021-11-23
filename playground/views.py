from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
# takes a request and returns a response, handles action

def say_hello(request):
    instance = Item(name='Raj', price=12, description='hello')
    instance.save()
    return render(request, 'hello.html',{'name': 'Raj'})