# Generated by Django 4.1.3 on 2022-11-24 10:34

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_description_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]
