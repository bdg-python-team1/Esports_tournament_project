from django.shortcuts import render
from . models import Tournament

def home(request):
    tournament_list = Tournament.objects.all()
    context_dict = {}
    context_dict['tournaments'] = tournament_list
    return render(request, 'tournaments/home.html', context_dict)


def host(request):
    return render(request, 'tournaments/host_a_tournament.html')

def show_tournament(request, category_name_slug):
    context_dict = {}
    try:
        tournament = Tournament.objects.get(slug=category_name_slug)
        context_dict['tournaments'] = tournament
    except Tournament.DoesNotExist:
        context_dict['tournaments'] = None

    return render(request, 'tournaments/tour.html', context_dict)