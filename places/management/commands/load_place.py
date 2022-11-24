from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Place


class Command(BaseCommand):
    help = "Add places on map"
    
    def handle(self, *args, **options):
        if options["url"]:
            url = options["url"]
            response = requests.get(url)
            response.raise_for_status()
            place = response.json()
            new_place = Place.objects.get_or_create(
                title = place["title"],
                description_short = place["description_short"],
                description_long=place["description_long"],
                lon = place["coordinates"]["lng"],
                lat = place["coordinates"]["lat"]
            )
            image_links = place["imgs"]
            for image_id, image_link in enumerate(image_links, start=1):
                response = requests.get(image_link)
                response.raise_for_status()
                image_file = ContentFile(response.content)
                image = new_place[0].images.get_or_create(
                    place=new_place,
                    image_id=image_id
                )
                image[0].image.save(
                    f"image_{image_id}.jpg", 
                    image_file, 
                    save=True
                )

    def add_arguments(self, parser):
        parser.add_argument(
            nargs="?",
            type=str,
            dest="url"
        )

