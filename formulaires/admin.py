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
    list_display=('libelle','code')
    list_per_page=settings.LIST_PER_PAGE
    
admin.site.register(Compagnies,CompagnieAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Pays,PaysAdmin)
admin.site.site_header = 'Gestion des colis v1'
