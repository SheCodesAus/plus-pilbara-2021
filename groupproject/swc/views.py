from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule
from .forms import ParticipantForm

def index(request):
    return render(request, 'swc/index.html')

def alumni (request):
    return render(request, 'swc/alumni.html')

def sponsors (request):
    return render(request, 'swc/index.html')

def pathways (request):
    return HttpResponse("You're looking at question.")

def stats (request):
    return render(request, 'swc/index.html')

# class AddLocationView(Generic.CreateView):
#     form_class = LocationForm
#     context_object_name = 'locationForm'
#     template_name = 'swc/index.html'
#     success_url = reverse_lazy('swc:index')

class AlumniView(generic.DetailView):
    model = Participant
    template_name = 'swc/participant.html'
    context_object_name = 'story'

class AddParticipantView(generic.CreateView):
    form_class = ParticipantForm
    context_object_name = 'participantForm'
    template_name = 'swc/createParticipant.html'
    success_url = reverse_lazy('swc:index')
