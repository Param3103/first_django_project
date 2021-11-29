from django.db import models
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow  = datetime.datetime.now()
    fileName = "%s%s", (timeNow, old_filename)
    return os.path.join("uploads/", filename)
# Create your models here.
class Item(models.Model):
    name = models.TextField(max_length=2700)
    age = models.TextField(max_length=2700)