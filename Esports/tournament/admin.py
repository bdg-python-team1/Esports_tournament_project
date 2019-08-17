from django.contrib import admin
from .models import Contest

# Register your models here.
class ContestAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Contest, ContestAdmin)