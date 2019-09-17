from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    player1 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player2 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    score1 = forms.IntegerField(initial=0)
    score2 = forms.IntegerField(initial=0)
    CHOICES = (
        (1, 'Quarter'),
        (2, 'Semifinal'),
        (3, 'Final'),
    )
    round = forms.ChoiceField(choices=CHOICES, help_text="Please, select from the below")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Match
        fields = ('player1', 'player2', 'score1', 'score2', 'round')
