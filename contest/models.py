from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Tournament(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, default='GevorgArtenyan')
    name = models.CharField(max_length=250, default='')
    player1 = models.CharField(max_length=250, default='')
    player2 = models.CharField(max_length=250, default='')
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tournament-detail', kwargs={'pk':self.pk})

class Result(models.Model):
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)