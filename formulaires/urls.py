from django.urls import path
from . import views
from .views import GetVilleView,GetCommuneView,GetDelay,GetPrice,GetPoids,GetSearchColis,GetSearchColis_List

urlpatterns=[
    path('',views.index,name='index'),
    path('colis/',views.colis,name='colis'),
    path('a_propos/',views.a_propos,name='a_propos'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('search_engine',views.search_engine,name='search_engine'),
    path('get_ville/<str:pays>',GetVilleView.as_view(),name='villes'),
    path('get_commune/<str:ville>',GetCommuneView.as_view(),name='communes'),
    path('get_delay/<str:delay>',GetDelay.as_view(),name='delay'),
    path('get_product/<str:product>',GetPrice.as_view(),name='product'),
    path('get_poids_price/<str:poids_price>',GetPoids.as_view(),name='poids_price'),
    path('search/<str:search>',GetSearchColis.as_view(),name='search'),
    path('search_list/<str:phone>',GetSearchColis_List.as_view(),name='search_list'),
    path('cr/',views.cr,name="cr"),
    path('get_colis_clos/<str:id_livraison>/<str:num_colis>',views.changColis_stt,name='colis_stt'),
    path('mail_sender/',views.mail_send,name='mail_sender'),
    
    
 ]