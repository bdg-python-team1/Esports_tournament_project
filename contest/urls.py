from django.urls import path
from . import views
from .views import TournamentListView, TournamentDetailView, TournamentCreateView, TournamentUpdateView, TournamentDeleteView

urlpatterns = [
    path('', TournamentListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('tournament/new/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournament/<int:pk>/update', TournamentUpdateView.as_view(), name='tournament-update'),
    path('tournament/<int:pk>/delete', TournamentDeleteView.as_view(), name='tournament-delete'),

]