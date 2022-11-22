from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Villes,Communes

def index(request):
   return HttpResponse("<h1>Page de gestion de colis</h1>")

class GetVilleView(View):
    def get(self,request,pays,*args, **kwargs):
        if request.is_ajax():
            villes=Villes.objects.filter(pays=pays).values('id','libelle')
            return JsonResponse({'data':list(villes)})
        return HttpResponse('Wrong request')

class GetCommuneView(View):
    def get(self,request,ville,*args, **kwargs):
        if request.is_ajax():
            communes=Communes.objects.filter(villes=ville).values('id','libelle')
            return JsonResponse({'data':list(communes)})
        return HttpResponse('Wrong request')
