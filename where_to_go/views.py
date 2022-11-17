from django.http import HttpResponse
from django.template import loader
from places.models import Place


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
                "coordinates": [float(place.lon), float(place.lat)]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
			    "detailsUrl": "static/moscow_legends.json"
            }
        })
    template = loader.get_template('index.html')
    context = {"json_data": geojson_points} 
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
