from django import forms
from .models import Flight



class FlightsForm(forms.ModelForm):


    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
           'departure_time' : forms.DateTimeInput(attrs={'type':'datetime-local'}),
           'landing_time' : forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
        labels = {
            'airline_company' : 'Airline Company',
            'origin_country' : 'Origin Country',
            'destination_country' : 'Destination Country'
        }









