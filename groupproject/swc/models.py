from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE

GENDER_CHOICES = [
('F','Female'),
('M','Male'),
('N','Non-Binary'),
('O','Other'),
]

STATE_CHOICES = [
('WA','WESTERN AUST'),
('QLD','QUEENSLAND'),
('NT','NORTHERN TERRITORY'),
('ACT','AUST CAPITAL TERRITORY'),
('SA','SOUTH AUST'),
('NSW','NEW SOUTH WALES'),
('VIC','VICTORIA'),
('EXT','EXTERNAL TERRITORIES'),
]

SPONSOR_TIER = [
('PL','PLATNIUM'),
('G','GOLD'),
('S','SILVER'),
('B','BRONZE'),
]

class Location(models.Model):
    state = models.CharField(max_length=5, choices=STATE_CHOICES)
    region = models.CharField(max_length=300)
    long = models.FloatField()
    lat = models.FloatField()
    def __str__(self):
        return self.state

class Language(models.Model):
    name = models.CharField(max_length=50)
    constraned_by = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Course(models.Model):
    program = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)
    date_started = models.DateTimeField()
    date_completed = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.program

class Completion_status(models.Model):
    course = models.ManyToManyField(Course)
    completion_date = models.DateTimeField()
    completion_result = models.CharField(max_length=50)
    def __str__(self):
        return self.completion_result


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    home_location = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    profile_pic = models.URLField()
    bio = models.TextField()
    tech_life_balance = models.CharField(max_length=30)
    in_mentor = models.CharField(max_length=30) 
    course = models.ManyToManyField(Course)
    completion = models.ManyToManyField(Completion_status)
    language = models.ManyToManyField(Language)
    def __str__(self):
        return self.first_name

class Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    language = models.ManyToManyField(Language)
    start_date = models.DateTimeField()
    def __str__(self):
        return self.location.region 

class Sponsors(models.Model):
    sponsor_name = models.CharField(max_length=50)
    logo_url = models.URLField()
    sponsor_tier = models.CharField(max_length=5, choices=SPONSOR_TIER)
    def __str__(self):
        return self.sponsor_name






