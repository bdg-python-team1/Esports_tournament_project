from django.shortcuts import render
from . models import Contest
from tournament.forms import ContestForm
def home(request):
    contest_list = Contest.objects.all()
    context_dict = {}
    context_dict['contests'] = contest_list
    return render(request, 'tournament/home.html', context_dict)


def host(request):
    form = ContestForm()
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'tournament/add_contest.html', {'form': form})

def show_contest(request, contest_name_slug):
    context_dict = {}
    try:
        contest = Contest.objects.get(slug=contest_name_slug)
        context_dict['contest'] = contest
    except Contest.DoesNotExist:
        context_dict['contest'] = None

    return render(request, 'tournament/contest.html', context_dict)

def add_contest(request):
    form = ContestForm()
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)

    return render(request, 'tournament/add_contest.html', {'form': form})


