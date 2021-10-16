from typing import Generic
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule

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

class AlumniView(DetailView):
    model = Participant
    template_name = 'swc/alumni.html'
    context_object_name = 'story'

