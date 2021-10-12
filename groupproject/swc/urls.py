from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'swc'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.alumni, name='alumni'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('stats/', views.stats, name='stats'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


