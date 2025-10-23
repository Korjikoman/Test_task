from django.shortcuts import render, get_object_or_404
from .models import Places
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
import html

def main_page(request):
    return render(request, 'index.html')


def places_geojson(request):
    """
    Функция возвращает все объекты из бд в Json формате.
    """
    features = []
    places = Places.objects.filter(lng__gt=-1, lat__gt=-1) # берем все подходящие значения из бд (которые есть на карте)

    for place in places:
        # добавляем в список features описание объекта в json-формате для фронта
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
    """
    Функция возращает json-response с подробным описанием объекта
    """
    place = get_object_or_404(Places, id=place_id) # получаем место
    clean_desc = html.unescape(place.description_long) # преобразуем символы &gt;, &#62;, &#x3e; и тд в юникод

    data = {
        "title": place.title,
        "description_short": place.description_short,
        "description_long": clean_desc,
        "imgs": [img.image.url for img in place.images.all()],
    }
    return JsonResponse(data)
