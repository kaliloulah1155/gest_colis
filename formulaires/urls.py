from django.urls import path
from . import views
from .views import GetVilleView,GetCommuneView

urlpatterns=[
    path('',views.index,name='index'),
    path('get_ville/<str:pays>',GetVilleView.as_view(),name='villes'),
    path('get_commune/<str:ville>',GetCommuneView.as_view(),name='communes')
 ]