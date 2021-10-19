from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from swc.views import AlumniView

app_name = 'swc'

urlpatterns = [
    path('', views.index, name='index'),
    path('participant/', views.AlumniView.as_view(), name='partipant'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('pathways/', views.PathwaysView.as_view(), name='pathways'),
    path('stats/', views.stats, name='stats'),
    # path('add-location/', views.AddLocationView.as_view(), name='locationView'),
    path('<int:pk>/', views.AlumniView.as_view(), name='story'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add-participant/', views.AddParticipantView.as_view(), name='participantView')
    
]


