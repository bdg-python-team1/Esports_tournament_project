# Generated by Django 2.2.3 on 2019-08-17 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='slug',
        ),
    ]