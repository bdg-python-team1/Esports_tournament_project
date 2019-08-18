from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('host/', views.host, name='host'),
    path('tournament/contest/<slug:contest_name_slug>/', views.show_contest, name='show_contest'),
    path('add_contest/', views.add_contest, name='add_contest'),
]