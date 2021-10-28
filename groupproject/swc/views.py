from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule, Sponsors,Completion_status,StudentCourse,KeyStatistics,ParticipantROI,SponsorROI
from .forms import ParticipantForm, ParticipantInterviewForm, StudentEnrollmentsForm
from django.db.models import Avg, aggregates, Count
import json

class IndexView(generic.ListView):
    template_name = 'swc/index.html'
    model = Participant

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        shecodes_statedata = { 
                'WA': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # ....
                    },
                },
                'SA': {
                    'regional': {
                        '1 day': 10
                    }
                }
        }
        json_data = json.dumps(shecodes_statedata)

        context = { "jsonData": json_data }
        return context

class PathwayView(generic.ListView):
    model = Course
    template_name = 'swc/pathways.html'
    context_object_name = 'pathways'

class AlumniView(generic.ListView):
    model = Participant
    template_name = 'swc/alumni.html'
    context_object_name = 'participants'

class AddParticipantView(generic.CreateView):
    form_class = ParticipantForm
    context_object_name = 'participantForm'
    template_name = 'swc/createParticipant.html'
    success_url = reverse_lazy('swc:index')

class ParticipantInterviewView(generic.CreateView):
    form_class = ParticipantInterviewForm
    context_object_name = 'participantInterviewForm'
    template_name = 'swc/participantInterview.html'
    success_url = reverse_lazy('swc:index')

class StudentEnrollmentView(generic.CreateView):
    form_class = StudentEnrollmentsForm
    context_object_name = 'studentEnrollmentsForm'
    template_name = 'swc/studentEnrollment.html'
    success_url = reverse_lazy('swc:index')


class SponsorView(generic.ListView):
    model = Sponsors
    template_name = 'swc/sponsors.html'
    context_object_name = 'sponsors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = Participant.objects.all().aggregate(Avg('age'))['age__avg']
        context['statsone'] = Participant.objects.count()
        context['stat'] = (context['statsone']/30)*100
        context['industries'] = Participant.objects.filter(industry__contains='MINING').count()
        context['upskilling'] = Participant.objects.filter(tech_life_balance__contains='working').count()

        return context 

    

