# Generated by Django 3.2.16 on 2022-11-20 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0012_add_colis'),
    ]

    operations = [
        migrations.AddField(
            model_name='colis',
            name='contact_receveur',
            field=models.CharField(default='0101010101', max_length=15, verbose_name='Contact du receveur'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 308176, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 308176, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 309178, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='date_arrive',
            field=models.DateField(verbose_name="Date d'arrivée"),
        ),
        migrations.AlterField(
            model_name='colis',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='colis',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 309178, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 308176, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='communes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 308176, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 302181, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='compagnies',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 302181, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 306176, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='pays',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 306176, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 307177, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='villes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 15, 18, 17, 307177, tzinfo=utc), verbose_name='Date de mise à jour'),
        ),
    ]