# Generated by Django 3.0.2 on 2020-01-08 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='replies',
        ),
    ]
