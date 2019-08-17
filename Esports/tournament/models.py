from django.db import models
from django.template.defaultfilters import slugify

class Tournament(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tournament, self).save(*args, **kwargs)

    def __str__(self):
        return self.name







# Create your models here.
