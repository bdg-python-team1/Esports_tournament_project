from django.shortcuts import render

def home(request):
    return render(request, 'tournament/home.html')


def host(request):
    return render(request, 'tournament/host_a_tournament.html')
