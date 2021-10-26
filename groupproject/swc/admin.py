from django.contrib import admin
from swc.models import Location, Language, Course, Participant, Schedule, Sponsors, Completion_status, KeyStatistics, ParticipantROI, SponsorROI, StudentCourse

class PaticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')

class LocationAdmin(admin.ModelAdmin):
    list_display =('state','region','long','lat')

class CourseAdmin(admin.ModelAdmin):
    list_display =('program','location','date_started','date_completed')

class LanguageAdmin(admin.ModelAdmin):
    list_display =('name',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display =('location', 'start_date')

class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('sponsor_name', 'sponsor_tier')

class Completion_statusAdmin(admin.ModelAdmin):
    list_display = ('completion_date', 'completion_result')

class KeyStatisticsAdmin(admin.ModelAdmin):
    list_display = ('social_reach', 'participation_target')

class ParticipantROIAdmin(admin.ModelAdmin):
    list_display = ('better_equipped', 'more_confident')

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('get_result', 'course_enrolled' )

class SponsorROIAdmin(admin.ModelAdmin):
    list_display = ('get_sponsor_name')

admin.site.register(Language, LanguageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Participant, PaticipantAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(KeyStatistics, KeyStatisticsAdmin)
admin.site.register(Completion_status, Completion_statusAdmin)
admin.site.register(ParticipantROI, ParticipantROIAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)









