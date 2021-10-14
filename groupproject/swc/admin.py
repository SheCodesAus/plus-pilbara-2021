from django.contrib import admin
from swc.models import Location, Language, Course, Participant, Schedule

class LocationAdmin(admin.ModelAdmin):
    fields = ['region', 'state']


admin.site.register(Location)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Participant)
admin.site.register(Schedule)


