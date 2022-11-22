# Generated by Django 3.2.16 on 2022-11-21 10:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0014_add_colis_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='colis',
            name='compagnie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulaires.compagnies', verbose_name='Compagnie de transport'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 761416, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 761416, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 762417, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 762417, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 761416, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 761416, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 756416, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 756416, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 759417, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 759417, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 760417, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 10, 59, 51, 760417, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]
