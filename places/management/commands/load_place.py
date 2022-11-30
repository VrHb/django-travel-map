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
            place_description = response.json()
            place_from_db, created = fill_db_place_description(
                place_description
            )
            if created:
                fill_db_place_images(place_description, place_from_db)

    def add_arguments(self, parser):
        parser.add_argument(
            nargs="?",
            type=str,
            dest="url"
        )


def fill_db_place_description(payload):
    place, created = Place.objects.get_or_create(
        title=payload["title"],
        defaults={
            "description_short": payload.get("description_short", ""),
            "description_long": payload.get("description_long", ""),
            "lon": payload["coordinates"]["lng"],
            "lat": payload["coordinates"]["lat"],
        }
    )
    return place, created 


def fill_db_place_images(place_description, place):
    image_links = place_description.get("imgs", [])
    for image_id, image_link in enumerate(image_links, start=1):
        response = requests.get(image_link)
        response.raise_for_status()
        image_file = ContentFile(
            response.content,
            f"{place.title}_{image_id}.jpg"
        )
        image, created = place.images.get_or_create(
            image_id=image_id,
            defaults={
                "place": place,
                "image": image_file
            }
        )
        if created is False:
            continue
