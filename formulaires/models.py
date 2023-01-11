from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError



# POUR LA COMPAGNIES
STATUS_CHOICES=(
    ('ac','Activé'),
    ('de','Desactivé')
)

# POUR LA CATEGORIES /SLUG
STATUS_CHOICES_SLUG=(
    ('produit','Produit'),
    ('WGT','Poids'),
    ('MP','Moyen de paiement'),
    ('TCL','Type de colis'),
    ('SV','Service'),
    ('DS','Etat livraison'),
    ('SM','Délai de livraison'),
)

class Compagnies(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    sigle = models.CharField(max_length=50,verbose_name="Sigle",blank=False,null=False)
    logo=models.FileField(upload_to='uploads/',blank=True,null=True)
    description = models.TextField(max_length=200,verbose_name="Description")
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    
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
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    class Meta:
        verbose_name_plural="Pays"
        verbose_name = "Pays"
    def __str__(self):
        return f"{self.libelle} - {self.code}"
    

##Villes
class Villes(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    pays=models.ForeignKey(Pays,verbose_name='Pays',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    class Meta:
        verbose_name_plural="Villes"
        verbose_name = "Ville"
    def __str__(self):
        return f"{self.libelle}"
    
##Communes
class Communes(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    villes=models.ForeignKey(Villes,verbose_name='Ville',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    class Meta:
        verbose_name_plural="Communes"
        verbose_name = "Commune"
    def __str__(self):
        return f"{self.libelle}"
    
##Categories
class Categories(models.Model):
    libelle = models.CharField(max_length=200,verbose_name="Libellé",blank=False,null=False)
    valeur = models.IntegerField(verbose_name="Valeur",null=True)
    slug = models.SlugField(max_length=50,verbose_name="Slug",blank=False,null=False,choices=STATUS_CHOICES_SLUG)
    position = models.IntegerField(verbose_name="Position",null=True)
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    
    class Meta:
        verbose_name_plural="Categories"
        verbose_name = "Categorie"
    def __str__(self):
        return f"{self.libelle}"


#COLIS
def generate_num_colis():
    code =str(uuid.uuid4())[:10].replace('-','').lower()
    return code
    
class Colis(models.Model):   
    num_colis = models.CharField(max_length=100,verbose_name="N° Colis",null=True)
    poids = models.IntegerField(verbose_name="Poids",null=True)
    receveur = models.CharField(max_length=200,verbose_name="Receveur",blank=False,null=False)
    adresse_receveur = models.CharField(max_length=200,verbose_name="Adresse du receveur",blank=False,null=False)
    contact_receveur = models.CharField(max_length=15,verbose_name="Contact du receveur",blank=False,null=False,default="0101010101")
    date_arrive = models.DateField(blank=False, null=False,verbose_name="Date d'arrivée")
    date_depart = models.DateField(blank=True, null=True,verbose_name="Date de départ")
    quartier = models.CharField(max_length=200,verbose_name="Quartier",blank=False,null=False)
    etape = models.IntegerField(verbose_name="Etape",null=True,default=0)
    type_table = models.CharField(max_length=5,verbose_name="Type Table",null=True,default='COL')
    photo=models.FileField(upload_to='uploads/',blank=False,null=False,verbose_name="Photo")
    user=models.ForeignKey(CustomUser,verbose_name='Créateur',blank=True,null=True,on_delete=models.CASCADE,)
    compagnie=models.ForeignKey(Compagnies,verbose_name='Compagnie de transport',blank=True,null=True,on_delete=models.CASCADE,)
    type_colis=models.ForeignKey(Categories,verbose_name='Type de colis',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    pays=models.ForeignKey(Pays,verbose_name='Pays',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},default=1)
    ville=models.ForeignKey(Villes,verbose_name='Villes',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    commune=models.ForeignKey(Communes,verbose_name='Communes',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
    admin_photo.short_description="Image"
    admin_photo.allow_tags=True
        
    def clean(self):
       # print(f"utilisateur : {CustomUser.objects.latest('id')}")
        if not self.photo:
             raise ValidationError("Veuillez selectionner une photo")
         
        if(self.date_arrive > self.date_depart):
            raise ValidationError("Attentation la date d'arrivée est supérieure à la date de départ")
    
    ''' def save(self, *args, **kwargs):
        self.num_colis = generate_num_colis()
        super(Colis, self).save(*args, **kwargs) '''
    def save(self, *args, **kwargs):
        if self.etape ==0:
            self.num_colis = generate_num_colis()
        super(Colis, self).save(*args, **kwargs)
    
        
    class Meta:
        verbose_name_plural="Colis"
        verbose_name = "Colis"
    def __str__(self):
        return f"Colis N° {self.num_colis}"
    
    
#LIVRAISONS
class Livraisons(models.Model):
    date_estimation = models.DateField(blank=True, null=True,verbose_name="Date de livraison")
    montant = models.IntegerField(verbose_name="Montant",blank=True,null=True,default=0)
    livreur=models.ForeignKey(CustomUser,verbose_name='Livreur',blank=True,null=True,on_delete=models.CASCADE,)
    moyen_paiement=models.ForeignKey(Categories,verbose_name='Moyen de paiement',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},)
    poids=models.ForeignKey(Categories,verbose_name='Poids',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='poids')
    delai=models.ForeignKey(Categories,verbose_name='Délai',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='delai')
    status_livraison=models.ForeignKey(Categories,verbose_name='Statut de la livraison',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='statut_livr')
    service=models.ForeignKey(Categories,verbose_name='Service',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='service')
    colis=models.ForeignKey(Colis,verbose_name='Colis',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='colis')
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    class Meta:
        verbose_name_plural="Livraisons"
        verbose_name = "Livraison"
    def __str__(self):
        return f"Livreur : {self.livreur}"
    
#COMPOSANTS / PRODUITS
class Composants(models.Model):
    produit=models.ForeignKey(Categories,verbose_name='Libellé',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='produit')
    pu = models.IntegerField(verbose_name="Prix unitaire",blank=True,null=True,default=0)
    qte = models.IntegerField(verbose_name="Quantité",blank=True,null=True,default=0)
    montant = models.IntegerField(verbose_name="Montant",blank=True,null=True,default=0)
    colis=models.ForeignKey(Colis,verbose_name='Colis',blank=True,null=True,on_delete=models.CASCADE,limit_choices_to={'status': True},related_name='colis_comp')
    status=models.BooleanField(default=True,verbose_name="Est Active")
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de création")
    updated_at = models.DateTimeField(default=timezone.now(),verbose_name="Date de mise à jour")
    
    class Meta:
        verbose_name_plural="Produits"
        verbose_name = "Produit"
    def __str__(self):
        return f"Produit : {self.produit.libelle}"

