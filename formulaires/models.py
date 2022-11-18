from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser




# POUR LA COMPAGNIES
STATUS_CHOICES=(
    ('ac','Activé'),
    ('de','Desactivé')
)

class Compagnies(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    sigle = models.CharField(max_length=50,verbose_name="Sigle",blank=False,null=False)
    logo=models.FileField(upload_to='uploads/',blank=True,null=True)
    description = models.TextField(max_length=200,verbose_name="Description")
    status=models.BooleanField(default=True,verbose_name="Est Active")
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo.url))
    admin_photo.short_description="Photo"
    admin_photo.allow_tags=True
    
    class Meta:
        verbose_name_plural="Compagnies"
        verbose_name = "Compagnie"
    def __str__(self):
        return f"{self.sigle} - {self.libelle}"
    
    
#POUR LES UTILISATEURS
class CustomUser(AbstractUser):
    adresse=models.CharField(max_length=100,blank=True,verbose_name='Adresse de localisation')
    telephone=models.CharField(max_length=10,blank=True,null=False,unique=True,verbose_name='N° Téléphone')
    compagnie=models.ForeignKey(Compagnies,verbose_name='Compagnie',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    class Meta:
        verbose_name_plural="Utilisateurs"
        verbose_name = "Utilisateur"
    
    def __str__(self) :
        return f"{self.first_name} {self.last_name}"
    
##PAYS

class Pays(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    code = models.CharField(max_length=15,verbose_name="Code",blank=False,null=False)
    class Meta:
        verbose_name_plural="Pays"
        verbose_name = "Pays"
    def __str__(self):
        return f"{self.libelle} - {self.code}"
    


    

    