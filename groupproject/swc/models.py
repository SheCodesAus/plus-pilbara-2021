from django.db import models
from django.db.models import fields

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=30)
    home_location = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    profile_pic = models.URLField()
    bio = models.TextField(max_length=500)
    tech_life_balance = models.CharField(max_length=30)
    in_mentor = models.CharField(max_length=30)

class Course(models.Model):
    program = models.CharField(max_length=50)
    date_started = models.DateTimeField()
    date_completed = models.DateTimeField()
    location = models.CharField(max_length=50)

class Paticipant_Course(models.Model):
    participation = models.CharField(max_length=50)
    Courses = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Location(models.Model):
    region = models.CharField(max_length=30)
    state = models.CharField(max_length=5)

class Language(models.Model):
    name = models.CharField(max_length=50)

class Participant_language(models.Model):
    Languages = models.CharField(max_length=50)
    participant = models.CharField(max_length=200)

class Schedule(models.Model):
    location = models.CharField(max_length=50))
    Courses = models.CharField(max_length=200)
    Languages = models.IntegerField(default=0)
    date = models.CharField(max_length=30)


    






