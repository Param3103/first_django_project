# Generated by Django 3.2.9 on 2021-12-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20211129_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='age',
            field=models.TextField(max_length=2700),
        ),
    ]
