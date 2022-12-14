# Generated by Django 3.2.16 on 2022-11-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0003_tel_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200, verbose_name='Libellé')),
                ('code', models.CharField(max_length=15, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Pays',
                'verbose_name_plural': 'Pays',
            },
        ),
    ]
