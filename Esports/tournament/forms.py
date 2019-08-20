from django import forms
from tournament.models import Contest, Match

class ContestForm(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text="Please enter the contest name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    player1 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player2 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player3 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player4 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player5 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player6 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player7 = forms.CharField(max_length=250, help_text="Enter a player name: ")
    player8 = forms.CharField(max_length=250, help_text="Enter a player name: ")


    class Meta:
        model = Contest
        fields = ('name', 'player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8')


class MatchForm(forms.ModelForm):
    score1 = forms.CharField(max_length=250, help_text="Enter a the score: ")
    score2 = forms.CharField(max_length=250, help_text="Enter a the score: ")
    score3 = forms.CharField(max_length=250, help_text="Enter a the score: ")
    score4 = forms.CharField(max_length=250, help_text="Enter a the score: ")

    class Meta:
        model = Match
        fields = ('score1', 'score2', 'score3', 'score4')