from django.contrib import admin
from django.conf import settings
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db.models import F
from django.utils.html import format_html


#Customization of admin user
class CustomUserAdmin(UserAdmin):
    ##add_form_template='gest_colis/admin/add_form.html'
    add_form = UserCreationForm
    form=UserChangeForm
    model=CustomUser
    list_display=['id','username','first_name','last_name','telephone']
    list_filter=('telephone',)
    #form of add
    add_fieldsets=UserAdmin.add_fieldsets + (
         (None,{'fields':('email','first_name','last_name','telephone','adresse','compagnie')}),
    )
    
    #form of edit
    fieldsets= ((None, {'fields': ('username', 'password')}),
     ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email','telephone','adresse','compagnie')}),
     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
     ('Dates importantes', {'fields': ('last_login', 'date_joined')}))
    list_per_page=settings.LIST_PER_PAGE
    

# Register your models here.
class CompagnieAdmin(admin.ModelAdmin):
    list_display=('libelle','sigle','status','admin_photo')
    list_filter=('sigle',)
    readonly_fields=('admin_photo',)
    list_per_page=settings.LIST_PER_PAGE
    
    
# Register your models here.
class PaysAdmin(admin.ModelAdmin):
    list_display=('libelle','code','status')
    list_per_page=settings.LIST_PER_PAGE
    
class VilleAdmin(admin.ModelAdmin):
    list_display=('libelle','pays','status')
    list_filter=('pays',)
    list_per_page=settings.LIST_PER_PAGE
    
class CommuneAdmin(admin.ModelAdmin):
    list_display=('libelle','villes','status')
    list_filter=('villes',)
    list_per_page=settings.LIST_PER_PAGE
    
class CategorieAdmin(admin.ModelAdmin):
    list_display=('libelle','valeur','slug','status')
    list_filter=('slug',)
    list_per_page=settings.LIST_PER_PAGE

class LivraisonInline(admin.TabularInline):
    model = Livraisons
    fieldsets=(
        (None,{
            'fields':('date_estimation','poids','montant','livreur','moyen_paiement','delai','status_livraison','service'),
        }),
    )
    can_delete = False
    max_num = 1
    def has_delete_permission(self, request, obj=None):
        return False
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "delai":
            kwargs["queryset"] = Categories.objects.filter(slug='SM').order_by(F('libelle').asc(nulls_last=True))  #MDelai de paiement
        if db_field.name == "poids":
            kwargs["queryset"] = Categories.objects.filter(slug='WGT').order_by(F('libelle').asc(nulls_last=True))  #MPoids de la livraison
        if db_field.name == "status_livraison":
            kwargs["queryset"] = Categories.objects.filter(slug='DS')  #Statut de la livraison
        if db_field.name == "moyen_paiement":
            kwargs["queryset"] = Categories.objects.filter(slug='MP')  #Moyen de paiement 
        if db_field.name == "service":
            kwargs["queryset"] = Categories.objects.filter(slug='SV')  #Moyen de paiement 
        if db_field.name == "livreur":
            kwargs["queryset"] = CustomUser.objects.filter(groups=1)  #Recuperation des livreurs
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

class ProduitInline(admin.TabularInline):
    model = Composants
    fieldsets=(
        (None,{
            'fields':('produit','pu','qte','montant'),
        }),
    )
    
    extra = 1
    list_per_page=settings.LIST_PER_PAGE
    @admin.display(
        description='Produit',
    )
    def produit_lib(self,obj):
        return obj.produit.libelle
    
    def produit_valeur(self,obj):
        return obj.produit.valeur
    produit_valeur.short_description = "Prix unitaire"
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "produit":
            kwargs["queryset"] = Categories.objects.filter(slug='produit').order_by(F('libelle').asc(nulls_last=True))  #MDelai de paiement
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class IsEtatColisFilter(admin.SimpleListFilter):
    title = 'Etat des colis'
    parameter_name = 'etape'
    def lookups(self, request, model_admin):
        return (
            (0, 'En cours'),
            (1, 'Transféré'),
            (2, 'Clos'),
            (3, 'Annulée'),
        )
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(etape=0)
        if self.value() == '1':
            return queryset.filter(etape=1)
        if self.value() == '2':
            return queryset.filter(etape=2)
        if self.value() == '3':
            return queryset.filter(etape=3)

class ColisAdmin(admin.ModelAdmin):
    list_display=('num_colis','date_arrive','date_depart','receveur','admin_photo','status','etat_colis',)
    list_filter=('date_arrive',IsEtatColisFilter)
    readonly_fields=('num_colis','type_table','etape','admin_photo','user','compagnie')
    change_form_template="admin/colis/change_form.html"
    fieldsets=(
        ('Coordonnées',{
            'fields':('poids','receveur','adresse_receveur','contact_receveur','date_arrive','date_depart',
                      'photo','pays','ville','commune','quartier'),
        }),
        ('Information Complémentaire',{
            'classes':('collapse',),
            'fields':('num_colis','etape','admin_photo','user','compagnie')
        })
    )
    inlines = [
        LivraisonInline,
        ProduitInline
    ]
    
    list_per_page=settings.LIST_PER_PAGE
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "type_colis":
            kwargs["queryset"] = Categories.objects.filter(slug='TCL')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        #print(f"{request.user.groups.all()[0].id}")
        if request.user.is_superuser: #Afficher tous les colis Pour l'ADMIN
            return qs
        if request.user.groups.all()[0].id==3: #Afficher tous les colis Pour la secretaire
            return qs
        return qs.filter(compagnie=request.user.compagnie) #Afficher tous les colis Pour le gestionnaire de colis
    
    def save_model(self, request, obj, form, change):
       # print(f"user_id {request.user.id} - compagnie {request.user.compagnie}")
        obj.user = request.user
        obj.compagnie = request.user.compagnie
        super().save_model(request, obj, form, change)
    
    def response_change(self, request, obj):
        if "_trans-colis" in request.POST:
            obj.etape = 1
            obj.save()
            #print (f" etape : {obj.etape}")
            self.message_user(request, "Colis transféré avec succès.")
        return super().response_change(request, obj)
    
    def etat_colis(self,obj):
        message_etape='En cours'
        message_bg_color='white'
        message_color='white'
        if(obj.etape==0): 
            message_etape='En cours'
            message_bg_color="blue"
        if(obj.etape==1): 
            message_etape='Transféré'
            message_bg_color='lightgreen'
            message_color='black'
        if(obj.etape==2): 
            message_etape='Clos'
            message_bg_color="#FF552A"
        if(obj.etape==3): 
            message_etape='Annulé'
            message_bg_color="#FF552A"
        return format_html(
            '<span style="background-color:{};color:{};padding-left: 1rem;padding-right: 1rem;">{}</span>',
            message_bg_color,
            message_color,
            message_etape
        )
    etat_colis.short_description = "Etat du colis"
          
        
class LivraisonsAdmin(admin.ModelAdmin):
    list_display=('id','date_estimation','poids','montant_format','livreur','moyen_paiement','delai','status_livraison','service','status')
    readonly_fields=('colis',)
    autocomplete_fields = ['livreur']
    list_filter=('created_at',)
    list_per_page=settings.LIST_PER_PAGE
    change_list_template="admin/colis/change_list.html"
    def montant_format(self,obj):
        return f" {obj.montant:,}".replace(',',' ')
    montant_format.short_description = "Montant(F CFA)"
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "delai":
            kwargs["queryset"] = Categories.objects.filter(slug='SM').order_by(F('libelle').asc(nulls_last=True))  #MDelai de paiement
            #widget = super(CategorieAdmin, self).formfield_for_dbfield(db_field, request, **kwargs).widget
            #widget.attrs.update({'params_1': 'toto'})
            #print(db_field)
            #return db_field.formfield(widget=widget)
       # return super(CategorieAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "poids":
            kwargs["queryset"] = Categories.objects.filter(slug='WGT').order_by(F('libelle').asc(nulls_last=True))  #Poids
        if db_field.name == "status_livraison":
            kwargs["queryset"] = Categories.objects.filter(slug='DS')  #Statut de la livraison
        if db_field.name == "moyen_paiement":
            kwargs["queryset"] = Categories.objects.filter(slug='MP')  #Moyen de paiement 
        if db_field.name == "service":
            kwargs["queryset"] = Categories.objects.filter(slug='SV')  #Moyen de paiement 
        if db_field.name == "livreur":
            kwargs["queryset"] = CustomUser.objects.filter(groups=1)  #Recuperation des livreurs
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class ComposantsAdmin(admin.ModelAdmin):
    list_display=('id','produit_lib','produit_valeur','status')
    readonly_fields=('colis',)
    list_per_page=settings.LIST_PER_PAGE
    @admin.display(
        description='Produit',
    )
    def produit_lib(self,obj):
        return obj.produit.libelle
    def produit_valeur(self,obj):
        return obj.produit.valeur
    produit_valeur.short_description = "Prix unitaire"
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "produit":
            kwargs["queryset"] = Categories.objects.filter(slug='produit').order_by(F('libelle').asc(nulls_last=True))  #MDelai de paiement
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        

#admin.site.register(Composants,ComposantsAdmin)


admin.site.register(Livraisons,LivraisonsAdmin)
admin.site.register(Compagnies,CompagnieAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Pays,PaysAdmin)
admin.site.register(Villes,VilleAdmin)
admin.site.register(Communes,CommuneAdmin)
admin.site.register(Categories,CategorieAdmin)
admin.site.register(Colis,ColisAdmin)
admin.site.site_header = "Gestion des colis"
admin.site.site_title = "Gestion des colis v1"
admin.site.index_title = "Bienvenue sur le site de gestion des colis"
