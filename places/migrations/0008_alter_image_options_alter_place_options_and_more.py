# Generated by Django 4.1.3 on 2022-11-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_options_place_sort_alter_image_upload'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={},
        ),
        migrations.RemoveField(
            model_name='place',
            name='sort',
        ),
        migrations.AddField(
            model_name='image',
            name='sort',
            field=models.PositiveIntegerField(default=0),
        ),
    ]