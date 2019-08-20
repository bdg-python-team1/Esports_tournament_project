from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('host/', views.host, name='host'),
    path('tournament/contest/<slug:contest_name_slug>/', views.show_contest, name='show_contest'),
    path('tournament/add_contest/', views.add_contest, name='add_contest'),
    path('tournament/contest/<slug:contest_name_slug>/add_match/', views.add_match, name='add_match')
]