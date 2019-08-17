from django.db import models
from django.template.defaultfilters import slugify

class Contest(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Contest, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
