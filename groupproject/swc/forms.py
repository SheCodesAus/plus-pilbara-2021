from django import forms
from django.forms import ModelForm, fields, models
from .models import Location, Language, Course, Participant, Schedule, Sponsors, Completion_status

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name','last_name','age','gender','home_location','phone','email','profile_pic','bio','tech_life_balance','in_mentor','course','completion','language']
