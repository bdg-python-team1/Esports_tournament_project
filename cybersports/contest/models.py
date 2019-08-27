from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Tournament(models.Model):
    name = models.CharField(max_length=250)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Match(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, default='GevorgArtenyan')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=250, default='')
    player2 = models.CharField(max_length=250, default='')
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.player1} {self.score1} : {self.score2} {self.player2}'

    def get_absolute_url(self):
        return reverse('match-detail', kwargs={'pk': self.pk})