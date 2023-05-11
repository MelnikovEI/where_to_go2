from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    data = {'points': {
        'type': 'FeatureCollection',
        'features': []
    }
    }
    for place in Place.objects.all():
        data['points']['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('place_description', args=[place.id])
                }
            }
        )
    return render(request, 'index.html', context=data)


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False, 'indent': 4})
