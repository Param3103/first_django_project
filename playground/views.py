from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
import requests

# Create your views here.
# takes a request and returns a response, handles action

def say_hello(request):
    instance = Item(name='Raj', price=12, description='hello')
    instance.save()
    r = requests.get('https://www.womenlines.com/')
    print(r.text)
    return render(request, 'hello.html',{'name': 'Charu, I got your websites code'})