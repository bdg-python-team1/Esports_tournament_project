# Generated by Django 2.2.3 on 2019-09-17 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('player1', models.CharField(max_length=150)),
                ('player2', models.CharField(max_length=150)),
                ('player3', models.CharField(max_length=150)),
                ('player4', models.CharField(max_length=150)),
                ('player5', models.CharField(max_length=150)),
                ('player6', models.CharField(max_length=150)),
                ('player7', models.CharField(max_length=150)),
                ('player8', models.CharField(max_length=150)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.CharField(default='', max_length=250)),
                ('player2', models.CharField(default='', max_length=250)),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Tournament')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
