from django.contrib import admin
from django.conf import settings
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



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

class ColisAdmin(admin.ModelAdmin):
    list_display=('num_colis','date_arrive','date_depart','receveur','admin_photo','status')
    list_filter=('date_arrive',)
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
    list_per_page=settings.LIST_PER_PAGE
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "type_colis":
            kwargs["queryset"] = Categories.objects.filter(slug='TCL')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
       # print(f"user_id {request.user.id} - compagnie {request.user.compagnie}")
        obj.user = request.user
        obj.compagnie = request.user.compagnie
        super().save_model(request, obj, form, change)
    
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
