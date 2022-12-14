# Generated by Django 3.2.16 on 2022-11-18 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0005_add_villes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200, verbose_name='Libellé')),
                ('villes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulaires.villes', verbose_name='Ville')),
            ],
            options={
                'verbose_name': 'Commune',
                'verbose_name_plural': 'Communes',
            },
        ),
    ]
