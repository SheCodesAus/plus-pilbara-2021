from django import forms
from django.forms import ModelForm, fields, models
from .models import Participant,StudentCourse,ParticipantROI

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name','last_name','age','gender','home_location','phone','email','profile_pic','bio','tech_life_balance','in_mentor','industry','language']

class ParticipantInterviewForm(ModelForm):
    class Meta:
        model = ParticipantROI
        fields = ['participant','course','better_equipped','more_confident','pursue_tech_career','another_course','interested_mentor']

class StudentEnrollmentsForm(ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['student','course','location']
