from django.contrib import admin
from swc.models import Location, Language, Course, Participant, Schedule, Sponsors

class PaticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
class LocationAdmin(admin.ModelAdmin):
    list_display =('state','region','long','lat')


admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Participant, PaticipantAdmin)
admin.site.register(Schedule)
admin.site.register(Sponsors)
admin.site.register(Location,LocationAdmin)




