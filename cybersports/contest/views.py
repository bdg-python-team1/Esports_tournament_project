from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Match, Tournament
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


def home(request):
    tournament_list = Tournament.objects.all()
    context_dict = {}
    context_dict['message'] = "All Tournaments"
    context_dict['tournaments'] = tournament_list
    return render(request, 'contest/home.html', context_dict)


def tournament_detail(request, tournament_name_slug):
    context_dict = {}
    try:
        tournament = Tournament.objects.get(slug=tournament_name_slug)
        matches = Match.objects.filter(tournament=tournament)
        context_dict['matches'] = matches
        context_dict['tournament'] = tournament
    except Tournament.DoesNotExist:
        context_dict['tournament'] = None
        context_dict['matches'] = None

    return render(request, 'contest/tournament_detail.html', context_dict)


class TournamentCreateView(LoginRequiredMixin, CreateView):
    model = Tournament
    fields = ['name', 'player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class TournamentListView(ListView):
    model = Tournament
    template_name = 'contest/home.html'
    context_object_name = 'tournaments'
    ordering = ['-date_posted']




# class TournamentDetailView(TemplateView):
#     template_name = 'contest/tournament_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(TournamentDetailView, self).get_context_data(**kwargs)
#         # TournamentDetailView.objects.filter()
#         context['matches'] = Match.objects.all()
#         context['tournaments'] = Tournament.objects.filter('name')
#         return context


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    fields = ['player1', 'player2', 'score1', 'score2']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class MatchListView(ListView):
    model = Match
    template_name = 'contest/tournament_detail.html'
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








