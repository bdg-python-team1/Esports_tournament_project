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
    path('', TournamentListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('match/<int:pk>/', MatchDetailView.as_view(), name='match-detail'),
    path('match/new/', MatchCreateView.as_view(), name='match-create'),
    path('match/<int:pk>/update', MatchUpdateView.as_view(), name='match-update'),
    path('match/<int:pk>/delete', MatchDeleteView.as_view(), name='match-delete'),


    path('tournament/new/', TournamentCreateView.as_view(), name='tournament-create'),
]