from django.db import models
from tinymce.models import HTMLField



class Place(models.Model):
    title = models.CharField("Название места", max_length=200)
    description_short = models.TextField(
        "Краткое описание",
        blank=True,
    )
    description_long = HTMLField(
        "Описание",
        blank=True,
    )
    lon = models.FloatField(
        "Долгота",
    )
    lat = models.FloatField(
        "Широта",
    )

    def __str__(self):
        return self.title
    

class Image(models.Model):
    upload = models.ImageField(
        verbose_name="Картинка",
        upload_to="images/",
    ) 
    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        related_name="images",
        on_delete=models.CASCADE,
    )
    image_id = models.PositiveIntegerField(
        default=0,
    )
    
    class Meta:
        ordering = ["image_id"]

    def __str__(self):
        return f"{self.image_id} {self.place.title}"

