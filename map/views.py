from django.shortcuts import render, get_object_or_404
from .models import Places
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F

def main_page(request):
    return render(request, 'index.html')


def places_geojson(request):
    features = []
    places = Places.objects.filter(lng__gt=-1, lat__gt=-1)

    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(place.lng), float(place.lat)]
            },
            "properties": {
                "title": place.title,
                "placeId": str(place.id),
                "detailsUrl": f"/api/places/{place.id}/"  
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson, encoder=DjangoJSONEncoder)

def place_detail(request, place_id):
    place = get_object_or_404(Places, id=place_id)
    images = [img.image.url for img in place.images.all()]

    data = {
        "title": place.title,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "imgs": images,
    }
    return JsonResponse(data)