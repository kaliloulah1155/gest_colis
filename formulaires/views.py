from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("<h1>Page de gestion de colis</h1>")
