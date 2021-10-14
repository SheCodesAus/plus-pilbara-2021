from django.db import models
from django.db.models import fields


class Location(models.Model):
    region = models.CharField(max_length=30)
    state = models.CharField(max_length=5)

class Language(models.Model):
    name = models.CharField(max_length=50)

class Course(models.Model):
    program = models.CharField(max_length=50)
    date_started = models.DateTimeField()
    date_completed = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=30)
    home_location = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    profile_pic = models.URLField()
    bio = models.TextField()
    tech_life_balance = models.CharField(max_length=30)
    in_mentor = models.CharField(max_length=30)  
    language = models.ManyToManyField(Language )

class Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date = models.DateTimeField()




