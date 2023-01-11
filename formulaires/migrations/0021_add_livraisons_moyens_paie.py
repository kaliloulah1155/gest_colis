# Generated by Django 3.2.16 on 2022-11-23 12:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0020_add_livraisons'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraisons',
            name='moyen_paiement',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulaires.categories', verbose_name='Moyen de paiement'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 740924, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 740924, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 741924, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 741924, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 740003, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 740003, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 735924, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 735924, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 743185, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='livreur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Livreur'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 743185, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 738924, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 738924, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 738924, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 25, 4, 738924, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]
