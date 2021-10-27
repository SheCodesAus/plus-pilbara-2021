from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.utils import timezone

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
('TAS', 'TASMANIA'),
('EXT','EXTERNAL TERRITORIES'),
]

SPONSOR_TIER = [
('PL','PLATNIUM'),
('G','GOLD'),
('S','SILVER'),
('B','BRONZE'),
]

INDUSTRIES = [
('M', 'MINING'),
('AG', 'AGRICULTURE'),
('MN', 'MINING'),
('MF', 'MANUFACTURING'),
('UT', 'UTILITIES'),
('CS', 'CONSTRUCTION'),
('AR', 'ARTS AND RECREATION'),
('HC', 'HEALTH CARE'),
('ED', 'EDUCATION AND TRAINING'),
('PS', 'PROFESSIONAL SERVICES'),
('RE', 'REAL ESTATE'),
('TA', 'TOURISM AND ACCOMMODATION'),
('IT', 'INFORMATION AND MEDIA'),
('OT', 'OTHER'),
]

ENROL_CHOICES = [
    ('E', 'ENROLLED'),
    ('N', 'NOT YET COMPLETE'),
    ('Q', 'CANCELLED'),
    ('C', 'COMPLETE'),
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
    course_bio = models.TextField()
    course_img = models.URLField()

    def __str__(self):
        return self.program
    
    def course_language(self):
        return ",".join([str(p) for p in self.language.all()])  

class Completion_status(models.Model):
    commencement_date = models.DateTimeField(default=timezone.now())
    completion_date = models.DateTimeField(default=timezone.now())
    completion_result = models.CharField(max_length=50, choices=ENROL_CHOICES)
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
    language = models.ManyToManyField(Language)
    industry = models.CharField(max_length=50, choices=INDUSTRIES)
    def __str__(self):
        return self.first_name

class Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    language = models.ManyToManyField(Language)
    start_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.location.region 

class StudentCourse(models.Model):
    student = models.ForeignKey(Participant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completion_status = models.ForeignKey(Completion_status, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.first_name 

    def student_name(self):
        return self.student.first_name + " " + self.student.last_name    

    def course_location(self):
        return self.location.region
    
    def course_enrolled(self):
        return self.course.program

    def get_result(self):
        return self.completion_status.completion_result
    
    def get_complete_date(self):
        return self.completion_status.completion_date
    

class Sponsors(models.Model):
    sponsor_name = models.CharField(max_length=50)
    logo_url = models.URLField()
    sponsor_tier = models.CharField(max_length=5, choices=SPONSOR_TIER)
    sponsor_why = models.CharField(max_length=500)
    sponsor_industry = models.CharField(max_length=50, choices=INDUSTRIES)
    def __str__(self):
        return self.sponsor_name

class KeyStatistics(models.Model):
    social_reach = models.IntegerField()
    participation_target = models.IntegerField()
    def __int__(self):
        return self.social_reach

class ParticipantROI(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    better_equipped = models.IntegerField()
    more_confident = models.IntegerField()
    pursue_tech_career = models.IntegerField()
    another_course = models.IntegerField()
    interested_mentor = models.IntegerField()
    def __str__(self):
        return self.participant.first_name
 

class SponsorROI(models.Model):
    sponsor = models.ManyToManyField(Sponsors)
    engagement = models.IntegerField()
    support_tech_women = models.IntegerField()
    wider_tech_commitments = models.IntegerField()

    def get_sponsor_name(self):
        return ",".join([str(p) for p in self.sponsor.all()])





