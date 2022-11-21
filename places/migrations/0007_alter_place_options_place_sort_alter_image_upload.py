# Generated by Django 4.1.3 on 2022-11-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['sort']},
        ),
        migrations.AddField(
            model_name='place',
            name='sort',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Загрузить'),
        ),
    ]