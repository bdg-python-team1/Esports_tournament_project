from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Match, Tournament
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'tournaments': Tournament.objects.all(),
    }
    return render(request, 'contest/home.html', context)


class TournamentCreateView(LoginRequiredMixin, CreateView):
    model = Tournament
    fields = ['name']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    fields = ['player1', 'player2', 'score1', 'score2']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class TournamentListView(ListView):
    model = Tournament
    template_name = 'contest/home.html'
    context_object_name = 'tournaments'
    ordering = ['-date_posted']


class MatchListView(ListView):
    model = Match
    template_name = 'contest/match_list.html'
    context_object_name = 'matches'



class MatchDetailView(DetailView):
    model = Match





class MatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Match
    fields = ['name', 'player1', 'player2', 'score1', 'score2']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def test_func(self):
        match = self.get_object()
        if self.request.user == match.host:
            return True
        return False


class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    success_url = '/'

    def test_func(self):
        match = self.get_object()
        if self.request.user == match.host:
            return True
        return False


def about(request):
    return render(request, 'contest/about.html')

