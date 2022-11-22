# Generated by Django 4.1.3 on 2022-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_upload_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]