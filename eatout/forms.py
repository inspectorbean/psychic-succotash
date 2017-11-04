from django import forms

from .models import Dinner, Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'genre', 'address', 'lat', 'lon']
        labels = {'name': 'Restaurant Name', 'genre': 'Restaurant Type', 'address':'Restaurant Address', 'lat':'Restaurant Latitude (Optional)', 'lon':'Restaurant Longitude (Optional)'}

class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['date', 'restaurant', 'attendance', 'spent', 'e_mood', 't_mood']
        labels = {'date': 'Date of Dinner', 'restaurant': 'Restaurant', 'attendance': 'Number of People at Dinner', 'spent': "Total Spent", 'e_mood': 'Eric Mood', 't_mood': 'Tory Mood'}
