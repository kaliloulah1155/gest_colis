# Generated by Django 3.2.16 on 2022-11-19 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0010_add_dt_created_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200, verbose_name='Libellé')),
                ('valeur', models.IntegerField(null=True, verbose_name='Valeur')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('position', models.IntegerField(null=True, verbose_name='Position')),
                ('status', models.BooleanField(default=True, verbose_name='Est Active')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 41519, tzinfo=utc), verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 41519, tzinfo=utc), verbose_name='Date de mise à jour')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 40473, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 40473, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 34200, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 34200, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 38194, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 38194, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 39451, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 11, 39, 26, 39451, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]