import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Command adds places from json files to DB'

    def handle(self, *args, **options):
        json_response = requests.get(*options['json_url'])
        json_response.raise_for_status()
        place_details = json_response.json()
        place, created = Place.objects.get_or_create(
            title=place_details['title'],
            description_short=place_details['description_short'],
            description_long=place_details['description_long'],
            lng=place_details['coordinates']['lng'],
            lat=place_details['coordinates']['lat'],
        )
        if not created:
            return
        for img_url in place_details['imgs']:
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img = Image.objects.create(place=place)
            img.img.save('img', ContentFile(img_response.content), save=True)

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            nargs=1,
            help='Ссылка на json файл, содержащий информацию о местах вида: https://raw.git...Bizone.json'
        )
