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
                        '1 day': 300, # ....
                        'flash': 50, # ....
                        'plus': 40, # ....
                        'alumni_mentor': 40,
                    },
                    'metro': {
                        '1 day': 500, # ....
                        'flash':700, # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': 1000,
                        'alumni_mentor': 60, # ....
                    },
                },
                # 'WA': {
                #     'regional': {
                #         '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                #         'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                #         'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(), # ....
                #         'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="WA").exclude(studentcourse__location__region__contains="Perth").count(),
                #     },
                #     'metro': {
                #         '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # ....
                #         'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                #         'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(),
                #         'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="WA", studentcourse__location__region__contains="Perth").count(), # ....
                #     },
                # },
                'SA': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="SA").exclude(studentcourse__location__region__contains="Adelaide").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="SA").exclude(studentcourse__location__region__contains="Adelaide").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="SA").exclude(studentcourse__location__region__contains="Adelaide").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="SA").exclude(studentcourse__location__region__contains="Adelaide").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="SA", studentcourse__location__region__contains="Adelaide").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="SA", studentcourse__location__region__contains="Adelaide").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="SA", studentcourse__location__region__contains="Adelaide").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="SA", studentcourse__location__region__contains="Adelaide").count(), # ....
                    },
                },
                'NT': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="NT").exclude(studentcourse__location__region__contains="Darwin").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="NT").exclude(studentcourse__location__region__contains="Darwin").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="NT").exclude(studentcourse__location__region__contains="Darwin").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="NT").exclude(studentcourse__location__region__contains="Darwin").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="NT", studentcourse__location__region__contains="Darwin").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="NT", studentcourse__location__region__contains="Darwin").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="NT", studentcourse__location__region__contains="Darwin").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="NT", studentcourse__location__region__contains="Darwin").count(), # ....
                    },
                },
                'QLD': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="QLD").exclude(studentcourse__location__region__contains="Brisbane").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="QLD").exclude(studentcourse__location__region__contains="Brisbane").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="QLD").exclude(studentcourse__location__region__contains="Brisbane").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="QLD").exclude(studentcourse__location__region__contains="Brisbane").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="QLD", studentcourse__location__region__contains="Brisbane").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="QLD", studentcourse__location__region__contains="Brisbane").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="QLD", studentcourse__location__region__contains="Brisbane").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="QLD", studentcourse__location__region__contains="Brisbane").count(), # ....
                    },
                },
                'NSW': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="NSW").exclude(studentcourse__location__region__contains="Sydney").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="NSW").exclude(studentcourse__location__region__contains="Sydney").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="NSW").exclude(studentcourse__location__region__contains="Sydney").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="NSW").exclude(studentcourse__location__region__contains="Sydney").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="NSW", studentcourse__location__region__contains="Sydney").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="NSW", studentcourse__location__region__contains="Sydney").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="NSW", studentcourse__location__region__contains="Sydney").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="NSW", studentcourse__location__region__contains="Sydney").count(), # ....
                    },
                },
                'VIC': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="VIC").exclude(studentcourse__location__region__contains="Melbourne").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="VIC").exclude(studentcourse__location__region__contains="Melbourne").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="VIC").exclude(studentcourse__location__region__contains="Melbourne").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="VIC").exclude(studentcourse__location__region__contains="Melbourne").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="VIC", studentcourse__location__region__contains="Melbourne").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="VIC", studentcourse__location__region__contains="Melbourne").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="VIC", studentcourse__location__region__contains="Melbourne").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="VIC", studentcourse__location__region__contains="Melbourne").count(), # ....
                    },
                },
                'ACT': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="ACT").exclude(studentcourse__location__region__contains="Canberra").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="ACT").exclude(studentcourse__location__region__contains="Canberra").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="ACT").exclude(studentcourse__location__region__contains="Canberra").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="ACT").exclude(studentcourse__location__region__contains="Canberra").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="ACT", studentcourse__location__region__contains="Canberra").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="ACT", studentcourse__location__region__contains="Canberra").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="ACT", studentcourse__location__region__contains="Canberra").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="ACT", studentcourse__location__region__contains="Canberra").count(), # ....
                    },
                },
                'TAS': {
                    'regional': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="TAS").exclude(studentcourse__location__region__contains="Hobart").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="TAS").exclude(studentcourse__location__region__contains="Hobart").count(), # ....
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="TAS").exclude(studentcourse__location__region__contains="Hobart").count(), # ....
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="TAS").exclude(studentcourse__location__region__contains="Hobart").count(),
                    },
                    'metro': {
                        '1 day': Participant.objects.all().filter(studentcourse__course__program="Workshop", studentcourse__location__state="TAS", studentcourse__location__region__contains="Hobart").count(), # ....
                        'flash': Participant.objects.all().filter(studentcourse__course__program="Flash", studentcourse__location__state="TAS", studentcourse__location__region__contains="Hobart").count(), # .... statedata['wa'][metro][flash], statedata.wa.metro.flash
                        'plus': Participant.objects.all().filter(studentcourse__course__program="Plus", studentcourse__location__state="TAS", studentcourse__location__region__contains="Hobart").count(),
                        'alumni_mentor': Participant.objects.all().filter(in_mentor="yes", studentcourse__location__state="TAS", studentcourse__location__region__contains="Hobart").count(), # ....
                    },
                },

            }
        json_data = json.dumps(shecodes_statedata)

        context = { "jsonData": json_data }

        return context

class PathwayView(generic.ListView):
    model = Course
    template_name = 'swc/pathways.html'
    context_object_name = 'pathways'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)

        context['coursecount'] = Participant.objects.count()
        context['programcounter'] = Course.objects.values('program', 'course_img').annotate(students=Count('studentcourse'))
        coursedata = Course.objects.values('program', 'course_img').annotate(students=Count('studentcourse'))
        context['programcounter2'] = { course['program']: course for course in coursedata}
        context['languagecounter'] = Course.objects.values('language').annotate(students=Count('studentcourse'))

        # context['flash_participant_count'] = Participant.objects.filter(learnerpath__program='Flash').count()

        return context


class AlumniView(generic.ListView):
    model = Participant
    template_name = 'swc/alumni.html'
    context_object_name = 'participants'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['language'] = Participant.objects.values('language')
    #     return context

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
        context['industries'] = Participant.objects.filter(industry__startswith='M').count()
        context['upskilling'] = Participant.objects.filter(tech_life_balance__contains='working').count()

        return context 
