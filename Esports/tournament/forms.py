from django import forms
from tournament.models import Contest

class ContestForm(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text="Please enter the contest name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contest
        fields = ('name',)

