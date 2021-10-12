from django.contrib import admin
from swc.models import Course, Language, Location, Participant, Participant_language, Paticipant_Course, Schedule



class CodeAdmin(admin.ModelAdmin):

admin.site.register(Participant, Course, Paticipant_Course, Language, Participant_language, Schedule, Location)
