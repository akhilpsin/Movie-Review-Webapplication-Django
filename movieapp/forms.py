from django import forms
from . models import movie

class movie_form(forms.ModelForm):
    class Meta:
        model = movie
        fields = {'name','des','year','img'}