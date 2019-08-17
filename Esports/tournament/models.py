from django.db import models
from django.template.defaultfilters import slugify

class Tournament(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tournament, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
