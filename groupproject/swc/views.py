from django.shortcuts import render
from .models import Location, Language, Course, Participant, Schedule

def index(request):
    return render(request, 'swc/index.html')

def alumni (request):
    return render(request, 'swc/index.html')

def sponsors (request):
    return render(request, 'swc/index.html')

def stats (request):
    return render(request, 'swc/index.html')

# def detail(request):
#     return render(request, 'swc/index.html')

# def results(request, question_id):
#     return render(request, 'swc/index.html')

# def vote(request, question_id):
#     return render(request, 'swc/index.html')
