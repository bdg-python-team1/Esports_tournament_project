from django.urls import path
from . import views
from .views import (TournamentListView,
                    TournamentCreateView,
                    MatchListView,
                    MatchUpdateView,
                    MatchDeleteView,
                    MatchDetailView,
                    MatchCreateView)

urlpatterns = [
    path('', views.home, name='home'),
    path('tournament/<slug:tournament_name_slug>/', views.tournament_detail, name='tournament-detail'),
    path('new-tournament/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournament/<slug:tournament_name_slug>/create-match/', MatchCreateView.as_view(), name='match-create'),
    path('about/', views.about, name='about'),
    path('tournament/<slug:tournament_name_slug>/match/<int:pk>/', MatchDetailView.as_view(), name='match-detail'),

    path('match/<int:pk>/update', MatchUpdateView.as_view(), name='match-update'),
    path('match/<int:pk>/delete', MatchDeleteView.as_view(), name='match-delete'),



]