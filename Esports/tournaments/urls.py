from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('host/', views.host, name='host'),
    path('tournaments/<slug:category_name_slug>/', views.show_tournament, name='show_tournament'),
]