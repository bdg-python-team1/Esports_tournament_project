from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Tournament, Result
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'tournaments':Tournament.objects.all(),
    }
    return render(request, 'contest/home.html', context)


class TournamentListView(ListView):
    model = Tournament
    template_name = 'contest/home.html'
    context_object_name = 'tournaments'
    ordering = ['-date_posted']


class TournamentDetailView(DetailView):
    model = Tournament


class TournamentCreateView(LoginRequiredMixin, CreateView):
    model = Tournament
    fields = ['name', 'player1', 'player2', 'score1', 'score2']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class TournamentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tournament
    fields = ['name', 'player1', 'player2', 'score1', 'score2']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tournament = self.get_object()
        if self.request.user == tournament.host:
            return True
        return False


class TournamentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tournament
    success_url = '/'

    def test_func(self):
        tournament = self.get_object()
        if self.request.user == tournament.host:
            return True
        return False


def about(request):
    return render(request, 'contest/about.html')

