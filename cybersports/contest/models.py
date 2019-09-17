from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
import uuid


class Tournament(models.Model):
    name = models.CharField(max_length=250)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    player1 = models.CharField(max_length=150)
    player2 = models.CharField(max_length=150)
    player3 = models.CharField(max_length=150)
    player4 = models.CharField(max_length=150)
    player5 = models.CharField(max_length=150)
    player6 = models.CharField(max_length=150)
    player7 = models.CharField(max_length=150)
    player8 = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tournament, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/tournament/{self.slug}/"


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=250, default='')
    player2 = models.CharField(max_length=250, default='')
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f'{self.player1} {self.score1} : {self.score2} {self.player2}'

    def get_absolute_url(self):
        return reverse('tournament-detail', kwargs={'pk': self.pk})
