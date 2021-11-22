from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes a request and returns a response, handles action

def say_hello(request):
    return render(request, 'hello.html',{'name':'Param'})