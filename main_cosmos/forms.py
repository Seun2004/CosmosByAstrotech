from django import forms
from .models import *

# show add form
class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('name', 'description', 'year_of_Release', 'avgPlanet','image')
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ('comment','planet')
        
    