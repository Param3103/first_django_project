from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import LoginForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.
# takes a request and returns a response, handles action
# create
def create(request):
    instance = Item(name='Raj', price=12, description='hello')
    instance.save()
    r = requests.get('https://www.womenlines.com/')
    print(r.text)
    return render(request, 'hello.html',{'name': 'Charu, I got your websites code'})
# read
def read(request):
    r = Item.objects.get(name='Raj')
    print(r.name)
    return render(request, 'hello.html',{'name': 'Charu, I got your websites code'})
# update
def update(request):
    Item.objects.filter(name='Raj').update(name='Param')
    return render(request, 'hello.html', {'name': 'Charu, I got your websites code'})
# delete
def delete(request):
    instance = Item.objects.filter(name='Raj')
    instance.delete()
    return render(request, 'hello.html', {'name': 'Charu, I got your websites code'})
def thank_you(request):
    return render(request, 'thank_you.html')
def form_view(request):
    # instantiate form object with data sent from user
    print(request.POST)
    form = LoginForm()
    name = form.data.get("name")
    age = form.data.get("age")
    print(name)
    if form.is_valid():  # no errors
        # authenticate user and log them in
        name = form.cleaned_data.get("name")
        age = form.cleaned_data.get("age")
        print(name,age)
        instance = Item(name=name, age=age)
        instance.save()

    else:  # get request
        form = LoginForm()

    return render(request, 'hello.html', {'form': form})