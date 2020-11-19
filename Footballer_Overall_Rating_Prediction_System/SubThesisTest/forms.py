from django import forms
from .regression import player_name

name_list = tuple(player_name())
choice = [(i, i) for i in name_list]
choice = tuple(choice)


class SearchForm(forms.Form):
    player_name = forms.ChoiceField(choices=choice)

    class Meta:
        fields = ['player_name']



