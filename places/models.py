from django.db import models



class Place(models.Model):
    title = models.CharField("Название места", max_length=200)
    description_short = models.CharField(
        "Краткое описание",
        max_length=400,
        blank=True,
        null=True
    )
    description_long = models.TextField(
        "Описание",
        blank=True,
        null=True
    )
    lat = models.DecimalField(
        "Широта",
        max_digits=30,
        decimal_places=20,
        blank=True,
        null=True
    )
    lon = models.DecimalField(
        "Долгота",
        max_digits=30,
        decimal_places=20,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.title

class Image(models.Model):
    upload = models.ImageField(
        verbose_name="Загрузить",
        upload_to="static/images/",
        null=True,
        blank=True
    ) 
    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        related_name="images",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.id} {self.place.title}"
