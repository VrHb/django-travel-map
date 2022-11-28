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
            place_object = fill_db_place_description(place_description)
            fill_db_place_images(place_description, place_object)

    def add_arguments(self, parser):
        parser.add_argument(
            nargs="?",
            type=str,
            dest="url"
        )


def fill_db_place_description(place):
    place_object, created = Place.objects.get_or_create(
        title=place["title"],
        defaults={
            "description_short": place.get("description_short", ""),
            "description_long": place.get("description_long", ""),
            "lon": place.get("coordinates", "").get("lng", ""),
            "lat": place.get("coordinates", "").get("lat", ""),
        }
    )
    return place_object


def fill_db_place_images(place_description, place_object):
    image_links = place_description["imgs"]
    for image_id, image_link in enumerate(image_links, start=1):
        response = requests.get(image_link)
        response.raise_for_status()
        image_file = ContentFile(
            response.content,
            f"{place_object.title}_{image_id}.jpg"
        )
        image, created = place_object.images.get_or_create(
            image_id=image_id,
            defaults={
                "place": place_object,
                "image": image_file
            }
        )
        if created is False:
            continue

