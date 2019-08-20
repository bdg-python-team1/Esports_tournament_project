from django.db import models
from django.template.defaultfilters import slugify

class Contest(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)
    player1 = models.CharField(max_length=250, default='', unique=True)
    player2 = models.CharField(max_length=250, default='', unique=True)
    player3 = models.CharField(max_length=250, default='', unique=True)
    player4 = models.CharField(max_length=250, default='', unique=True)
    player5 = models.CharField(max_length=250, default='', unique=True)
    player6 = models.CharField(max_length=250, default='', unique=True)
    player7 = models.CharField(max_length=250, default='', unique=True)
    player8 = models.CharField(max_length=250, default='', unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Contest, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Match(models.Model):
    score1 = models.CharField(max_length=250, default='0:0')
    score2 = models.CharField(max_length=250, default='0:0')
    score3 = models.CharField(max_length=250, default='0:0')
    score4 = models.CharField(max_length=250, default='0:0')