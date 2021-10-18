from typing import Generic
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .models import Location, Language, Course, Participant, Schedule
import json

def index(request):
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
    context = { "jsonData": json_data }
    return render(request, 'swc/index.html', context)

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