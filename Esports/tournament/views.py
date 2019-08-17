from django.shortcuts import render
from . models import Tournament

def home(request):
    tournament_list = Tournament.objects.all()
    context_dict = {}
    context_dict['tournaments'] = tournament_list
    return render(request, 'tournament/home.html', context_dict)


def host(request):
    return render(request, 'tournament/host_a_tournament.html')

def show_tournament(request, category_name_slug):
    context_dict = {}
    try:
        tournament = Tournament.objects.get(slug=category_name_slug)
        context_dict['tournament'] = tournament
    except Tournament.DoesNotExist:
        context_dict['tournament'] = None

    return render(request, 'tournament/tour.html', context_dict)