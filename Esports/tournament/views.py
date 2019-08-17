from django.shortcuts import render
from . models import Contest

def home(request):
    contest_list = Contest.objects.all()
    context_dict = {}
    context_dict['contests'] = contest_list
    return render(request, 'tournament/home.html', context_dict)


def host(request):
    return render(request, 'tournament/host_a_tournament.html')

def show_contest(request, contest_name_slug):
    context_dict = {}
    try:
        contest = Contest.objects.get(slug=contest_name_slug)
        context_dict['contest'] = contest
    except Contest.DoesNotExist:
        context_dict['contest'] = None

    return render(request, 'tournament/contest.html', context_dict)