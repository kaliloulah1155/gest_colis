from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Villes,Communes,Categories,Colis,Livraisons,Composants
from .forms import SearchForm
from pycrystal import *
from itertools import chain
from django.core.serializers import serialize
import json
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os
from pathlib import Path


def index(request):
   return render(request,'index.html')

def search_engine(request):
   form = SearchForm()
   return render(request,'formulaires/search.html', {'form': form})

class GetVilleView(View):
    def get(self,request,pays,*args, **kwargs):
        if request.is_ajax():
           # print(request.user.groups.all()[0].id)
            villes=Villes.objects.filter(pays=pays).values('id','libelle')
            return JsonResponse({'data':list(villes)})
        return HttpResponse('Wrong request')

class GetCommuneView(View):
    def get(self,request,ville,*args, **kwargs):
        if request.is_ajax():
            communes=Communes.objects.filter(villes=ville).values('id','libelle')
            return JsonResponse({'data':list(communes)})
        return HttpResponse('Wrong request')

class GetDelay(View):
    def get(self,request,delay,*args, **kwargs):
        if request.is_ajax():
            delay_val=Categories.objects.filter(id=delay).values('id','valeur')
            return JsonResponse({'data':list(delay_val)})
        return HttpResponse('Wrong request')

class GetPrice(View):
    def get(self,request,product,*args, **kwargs):
        if request.is_ajax():
            product_val=Categories.objects.filter(id=product).values('id','valeur')
            return JsonResponse({'data':list(product_val)})
        return HttpResponse('Wrong request')

class GetPoids(View):
    def get(self,request,poids_price,*args, **kwargs):
        if request.is_ajax():
            product_val=Categories.objects.filter(id=poids_price).values('id','valeur')
            return JsonResponse({'data':list(product_val)})
        return HttpResponse('Wrong request')
    

class GetSearchColis(View):   
    def get(self,request,search,*args, **kwargs):
        #if request.is_ajax():
        if request:
            record = Colis.objects.filter(num_colis__contains=search)
            if(len(record)!=0):
                entries = Colis.objects.select_related('compagnie').filter(num_colis__contains=search)
                livraisons = Livraisons.objects.filter(colis__id=entries[0].id)
                if(len(entries) !=0):
                    data1 = [{
                        'num_colis': entry.num_colis if entry.num_colis else "NEANT" , 
                        'receveur': entry.receveur if entry.receveur else "NEANT",
                        'poids_rel': entry.poids if entry.poids else "NEANT",
                        'contact_receveur': entry.contact_receveur if entry.contact_receveur else "NEANT",
                        'adr_receveur': entry.adresse_receveur if entry.adresse_receveur else "NEANT", 
                        'pays': entry.pays.libelle if entry.pays else "NEANT", 
                        'compagnie_libelle': entry.compagnie.libelle if entry.compagnie else "NEANT",
                        'photo': entry.photo.url if entry.photo else "/static/sidi.jpg",
                        } for entry in entries ]   
                    
                    liv_data = json.loads( serialize("json", livraisons))
                    if(len(liv_data[0]) != 0):
                        liv_poids = json.loads(serialize('json',Categories.objects.filter(id=liv_data[0]["fields"]["poids"])))
                        liv_moypaie = json.loads(serialize('json',Categories.objects.filter(id=liv_data[0]["fields"]["moyen_paiement"])))
                        liv_st = json.loads(serialize('json',Categories.objects.filter(id=liv_data[0]["fields"]["status_livraison"])))
                    #Donnée de la livraison
                    dt_liv=[
                        {
                            'poids': liv_poids[0]["fields"]["libelle"] if len(liv_poids[0]) !=0 else "NEANT",
                            'moyen_paiement': liv_moypaie[0]["fields"]["libelle"] if len(liv_moypaie[0]) !=0 else "NEANT",
                            'status_livraison': liv_st[0]["fields"]["libelle"] if len(liv_st[0]) !=0 else "NEANT",
                            'montant': liv_data[0]["fields"]["montant"] if len(liv_data[0]) !=0 else "NEANT"
                        }
                    ]
                    data = list(chain(data1, dt_liv))
                    return JsonResponse({'results': data})
                else: return JsonResponse({'results': {"Ce colis n'existe pas"}})
            return JsonResponse({'error': "Ce colis n'existe pas"}, status=400)
        
class GetSearchColis_List(View):   
    def get(self,request,phone,*args, **kwargs):
        if request:
            data_colis = Colis.objects.filter(contact_receveur=phone)
            data = []
            if(len(data_colis)!=0):
                for x in data_colis:
                    data_livraisons = Livraisons.objects.filter(colis__id=x.id)
                    list_livraisons = []
                    for l in data_livraisons:
                        liv_poids = json.loads(serialize('json',Categories.objects.filter(id=l.poids.id)))
                        liv_moypaie = json.loads(serialize('json',Categories.objects.filter(id=l.moyen_paiement.id)))
                        liv_st = json.loads(serialize('json',Categories.objects.filter(id=l.status_livraison.id)))
                        list_livraisons.append({
                            'id':l.id,
                            'num_colis' : l.colis.num_colis,
                            'montant' : l.montant,
                            'poids' : liv_poids[0]["fields"]["libelle"] if len(liv_poids[0]) !=0 else "NEANT",
                            'moyen_paiement': liv_moypaie[0]["fields"]["libelle"] if len(liv_moypaie[0]) !=0 else "NEANT",
                            'status_livraison': liv_st[0]["fields"]["libelle"] if len(liv_st[0]) !=0 else "NEANT",
                        })
                    data_produits = Composants.objects.filter(colis__id=x.id)
                    list_produits = []
                    for p in data_produits:
                        pod_name = json.loads(serialize('json',Categories.objects.filter(id=p.produit.id)))
                        list_produits.append({
                            'id':p.id,
                            'libelle' : pod_name[0]["fields"]["libelle"] if len(liv_poids[0]) !=0 else "NEANT",
                            'pu':p.pu,
                            'qte':p.qte,
                            'montant':p.montant,
                        })
                    data.append({
                        'id' : x.id,
                        'num_colis' : x.num_colis,
                        'poids_rel' : x.poids,
                        'receveur' : x.receveur,
                        "adresse_receveur": x.adresse_receveur,
                        "contact_receveur": x.contact_receveur,
                        "date_arrive": x.date_arrive.strftime("%d/%m/%Y"),
                        "date_depart": x.date_depart.strftime("%d/%m/%Y"),
                        "quartier": x.quartier,
                        'image' : x.photo.url,
                        'pays' : x.pays.libelle,
                        'compagnie' : x.compagnie.libelle,
                        'livraisons':list_livraisons,
                        'produits':list_produits
                    })
                return JsonResponse(data,safe=False)
            return JsonResponse({'error': "Ce colis n'existe pas"}, status=400)
    

def changColis_stt(request,id_livraison,num_colis):
    if request.is_ajax():
        if id_livraison=='9' : ##si le colis est livré
           Colis.objects.filter(num_colis__contains=num_colis).update(etape=2)
        elif id_livraison=='29' : ##si le colis est Annulée
           Colis.objects.filter(num_colis__contains=num_colis).update(etape=3)
        else: Colis.objects.filter(num_colis__contains=num_colis).update(etape=1)
        
        return JsonResponse({'results': 'success'})
    return JsonResponse({'error': 'Invalid form'}, status=400)
    
def cr(request):
    return HttpResponse('Ok cool')
    
def colis(request):
    return render(request,'formulaires/colis.html')

def a_propos(request):
    return render(request,'formulaires/a_propos.html')

def contact(request):
    return render(request,'formulaires/contact.html')

def services(request):
    return render(request,'formulaires/services.html')

def mail_send(request):
    if request.method=='POST':
        #message = request.POST['message']
        #email = request.POST['email']
        #name = request.POST['name']
        
        subject="GESTION DES COLIS"
        from_email='settings.EMAIL_HOST_USER'
        to = "konateibrahim126@gmail.com"
        code_colis="pzasert"
        html_content = render_to_string('formulaires/mail.html', {'num_colis':code_colis}) # render with dynamic value
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.mixed_subtype = 'related'
        msg.attach_alternative(html_content, "text/html")
        img_dir = 'static'
        image = 'sidi.jpg'
        image_name = Path(image).name
        file_path = os.path.join(img_dir, image)
        #with open(file_path, 'rb') as f:
            #img = MIMEImage(f.read())
            #img.add_header('Content-ID', '<{name}>'.format(name=image_name))
            #img.add_header('Content-Disposition', 'inline', filename=image)
        #msg.attach(img)
        msg.send()
        return JsonResponse({'results': 'success send'})