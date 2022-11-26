from django.http import JsonResponse
from django.urls import reverse

from places.models import Place

from django.shortcuts import render, get_object_or_404


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_properties = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }
    return JsonResponse(
        place_properties,
        json_dumps_params={"ensure_ascii": False}
    )


def show_main(request):
    places = Place.objects.all()
    geojson_points = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        geojson_points["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": reverse("places", args=[place.id])
            }
        })
    return render(request, "index.html", {"json_data": geojson_points})
