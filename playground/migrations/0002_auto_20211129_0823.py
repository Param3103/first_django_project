# Generated by Django 3.2.9 on 2021-11-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='item',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]