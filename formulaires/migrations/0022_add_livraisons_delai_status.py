# Generated by Django 3.2.16 on 2022-11-23 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0021_add_livraisons_moyens_paie'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraisons',
            name='delai',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delai', to='formulaires.categories', verbose_name='Délai'),
        ),
        migrations.AddField(
            model_name='livraisons',
            name='status_livraison',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statut_livr', to='formulaires.categories', verbose_name='Statut de la livraison'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 534712, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 534712, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 535712, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 535712, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 533712, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 533712, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 527713, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 527713, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 537711, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='livreur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulaires.customuser', verbose_name='Livreur'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='moyen_paiement',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, to='formulaires.categories', verbose_name='Moyen de paiement'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 537711, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 532711, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 532711, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 533712, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 2, 37, 533712, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]
