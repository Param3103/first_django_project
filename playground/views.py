from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item,File_URL
from .forms import LoginForm
import requests
from django.core.files.storage import FileSystemStorage
import os

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
def registration_page(request):
    # instantiate form object with data sent from user
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():  # no errors
            # authenticate user and log them in
            try:
                form.save()
            except:
                pass
        else:
            form = LoginForm()

    return render(request, 'hello.html', {'form': form})
def display_registered_users(request):
    return render(request, "show.html", {'users': list(Item.objects.values())})

def delete_user(request, id):
    user = Item.objects.get(id=id)
    user.delete()
    return render(request, "show.html", {'users': list(Item.objects.values())})

def update_user(request, id):
    user = Item.objects.get(id=id)
    if request.method == 'POST':
        form = LoginForm(request.POST or None, instance=user)
        if form.is_valid():  # no errors
            # authenticate user and log them in
            try:
                form.save()
                return(redirect('../../show/'))
            except:
                pass
    else:
        form = LoginForm(instance=user)
        context = {
            'form': form
        }
        return render(request, 'update.html', context)
    return render(request, "update.html", {'users': list(Item.objects.values()), 'form':form})
def file_upload(request):
    print(request)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.path.abspath(fs.url(filename))
        instance = File_URL(path=uploaded_file_url)
        instance.save()
        return render(request, 'file_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'uploaded_file': filename,
        })
    return render(request, 'file_upload.html')
def test_cookie(request):
    response = HttpResponse("Visiting for the first time")
    if not request.COOKIES.get('team'):
        response.set_cookie('team', 'barcelona')
        return response
    else:
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
        return HttpResponse("Your favourite team is {}".format(request.COOKIES['team']))
