from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule
from .forms import ParticipantForm

def index(request):
    return render(request, 'swc/index.html')


def sponsors (request):
    return render(request, 'swc/index.html')

class PathwaysView(generic.TemplateView):
    template_name = 'swc/pathways.html'

def stats (request):
    return render(request, 'swc/index.html')

# class AddLocationView(Generic.CreateView):
#     form_class = LocationForm
#     context_object_name = 'locationForm'
#     template_name = 'swc/index.html'
#     success_url = reverse_lazy('swc:index')

class AlumniView(generic.ListView):
    model = Participant
    template_name = 'swc/alumni.html'
    context_object_name = 'participants'

class AddParticipantView(generic.CreateView):
    form_class = ParticipantForm
    context_object_name = 'participantForm'
    template_name = 'swc/createParticipant.html'
    success_url = reverse_lazy('swc:index')
