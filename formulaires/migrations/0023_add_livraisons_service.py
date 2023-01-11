# Generated by Django 3.2.16 on 2022-11-23 13:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0022_add_livraisons_delai_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraisons',
            name='service',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='formulaires.categories', verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 700645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 700645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 701645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 701645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 699645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 700645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 695645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 695645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 702645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='delai',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, related_name='delai', to='formulaires.categories', verbose_name='Délai'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='status_livraison',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, related_name='statut_livr', to='formulaires.categories', verbose_name='Statut de la livraison'),
        ),
        migrations.AlterField(
            model_name='livraisons',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 702645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 698645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 698645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 699645, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 13, 11, 25, 699645, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]