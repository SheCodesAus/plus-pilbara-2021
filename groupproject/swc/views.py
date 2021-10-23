from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule, Sponsors
from .forms import ParticipantForm, ParticipantInterviewForm
from django.db.models import Avg, aggregates, Count
import json

class IndexView(generic.ListView):
    template_name = 'swc/index.html'
    model = Participant
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        Shecode_statedata =  {
        "Western Australia": 1500,
        "Northern Territory": 0,
        "South Australia": 150,
        "Queensland": 600,
        "New South Wales": 40,
        "Australian Capital Territory":60,
        "Victoria":250,
        "Tasmania": 30,
        

        }
        json_data = json.dumps(Shecode_statedata)
        context["jsonData"]=json_data



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

    

