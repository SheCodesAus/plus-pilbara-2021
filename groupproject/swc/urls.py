from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from swc.views import AlumniView
from django.contrib.auth import views as auth_views

app_name = 'swc'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('alumni/', views.AlumniView.as_view(), name='participant'),
    path('sponsors/', views.SponsorView.as_view(), name='sponsors'),
    path('pathways/', views.PathwayView.as_view(), name='pathways'),
    path('add-participant/', views.AddParticipantView.as_view(), name='participantView'),
    path('participant-interview/', views.ParticipantInterviewView.as_view(), name='participantInterview'),
    path('enrol-student/', views.StudentEnrollmentView.as_view(), name='StudentEnrollmentsForm'),
    # path('log-out/', auth_views.logOutView.as_view())
]
