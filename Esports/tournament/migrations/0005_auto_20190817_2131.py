# Generated by Django 2.2.3 on 2019-08-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20190817_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
