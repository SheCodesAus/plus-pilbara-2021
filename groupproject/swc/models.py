from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE


class Location(models.Model):
    region = models.CharField(max_length=30)
    state = models.CharField(max_length=5)
    def __str__(self):
        return self.region + " / " + self.state

class Language(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Course(models.Model):
    program = models.CharField(max_length=50)
    date_started = models.DateTimeField()
    date_completed = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.program + " - " + self.location.region

GENDER_CHOICES = [
('F','Female'),
('M','Male'),
('N','Non-Binary'),
('O','Other'),
]

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    home_location = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    profile_pic = models.URLField()
    bio = models.TextField()
    tech_life_balance = models.CharField(max_length=30)
    in_mentor = models.CharField(max_length=30)  
    language = models.ManyToManyField(Language)
    def __str__(self):
        return self.first_name + " "+ self.last_name + self.gender

class Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    language = models.ManyToManyField(Language)
    date = models.DateTimeField()
    def __str__(self):
        return self.location.region 




