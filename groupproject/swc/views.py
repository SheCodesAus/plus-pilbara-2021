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
        context = super().get_context_data(**kwargs)
        # context['Australia_participants_total'] = Participant.objects.all().count()
        # context['state_participants_total'] = Participant.objects.filter(state="").count()

        # context['Australia_participants_by_course'] = Participant.objects.all().filter(Course).count()
        # context['state_participants_by_course'] = Participant.objects.filter(course__state="").count()

        # context['Australia_metro_participants_total'] = Participant.objects.all().filter(course__state__region="Perth"+"Adelaide"+"Darwin"+ "Brisbane"+"Sydney"+"Melbourne"+"Hobart"+"Canberra").count()
        # context['state_metro_participants_total'] = Participant.objects.filter(course__state="").count()

        # context['Australia_regional_participants_total'] = Participant.objects.exclude(course__location__region="").count()
        # context['state_regional_participants_total'] = Participant.objects.filter(course__state="").count()
    

        # hayley was here
        ## show total number = statedata.wa + state names?
        ## number by course
        ## number by state

        shecodes_statedata = { 
            'WA': {
                'regional': {
                    '1 day': Participant.objects.all().filter(course__program="Workshop", course__location__state="WA").exclude(course__location__region__contains="Perth").count(), # ....
                    'flash': Participant.objects.all().filter(course__program="Flash", course__location__state="WA").exclude(course__location__region__contains="Perth").count(), # ....
                    'plus': Participant.objects.all().filter(course__program="Plus", course__location__state="WA").exclude(course__location__region__contains="Perth").count(), # ....
                    'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", course__location__state="WA").exclude(course__location__region__contains="Perth").count(),
                },
                'metro': {
                    '1 day': Participant.objects.all().filter(course__program="Workshop", course__location__state="WA", course__location__region__contains="Perth").count(), # ....
                    'flash': Participant.objects.all().filter(course__program="Flash", course__location__state="WA", course__location__region__contains="Perth").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all().filter(course__program="Plus", course__location__state="WA", course__location__region__contains="Perth").count(),
                    'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", course__location__state="WA", course__location__region__contains="Perth").count(), # ....
                },
            },
            'SA': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'NT': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'QLD': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'NSW': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'VIC': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'ACT': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
            'TAS': {
                'regional': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # ....
                    'plus': Participant.objects.all(), # ....
                },
                'metro': {
                    '1 day': Participant.objects.all(), # ....
                    'flash': Participant.objects.all(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                    'plus': Participant.objects.all(), # ....
                },
            },
        }
        print(shecodes_statedata['WA']['regional']['1 day'])
        json_data = json.dumps(shecodes_statedata)
        context = { "jsonData": json_data }

        return context 
        # if someone clicked "1 day"
        # add wa 1 day + qld 1 day + nsw + 1 day....
  

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

    

