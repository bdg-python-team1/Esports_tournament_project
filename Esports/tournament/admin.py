from django.contrib import admin
from .models import Tournament

# Register your models here.
class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tournament, TournamentAdmin)