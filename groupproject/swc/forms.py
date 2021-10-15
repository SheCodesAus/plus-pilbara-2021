from django import forms
from django.forms import ModelForm
from .models import Location, Language, Course, Participant, Schedule

# class LocationForm(ModelForm):
#     class Meta:
#         model = Location
#         fields = ['State', 'Region']

#     def __init__(self,*args, **kwargs):
#         super(LocationForm, self).__init__(*args, **kwargs)
#         self.fields['title']({'class': 'title_class'})


