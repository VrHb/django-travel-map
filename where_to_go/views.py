from django.http import HttpResponse
from django.template import loader


def show_main(request):
    geojson_points = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
			    "detailsUrl": "static/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
			    "detailsUrl": "static/roofs24.json"
            }
        }]
    }
    template = loader.get_template('index.html')
    context = {"json_data": geojson_points} 
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
