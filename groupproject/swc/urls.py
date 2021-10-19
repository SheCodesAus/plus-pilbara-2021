from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from swc.views import AlumniView

app_name = 'swc'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.AlumniView.as_view(), name='participant'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('pathways/', views.pathways, name='pathways'),
    path('stats/', views.stats, name='stats'),
    path('add-participant/', views.AddParticipantView.as_view(), name='participantView')
    
]


