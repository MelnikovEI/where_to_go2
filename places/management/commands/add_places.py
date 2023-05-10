import json
import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from tqdm import tqdm

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Command adds places from json files to DB'

    def handle(self, *args, **options):
        places_info_folder = os.path.join(*options['folder'])
        for root, dirs, files in os.walk(places_info_folder):
            for file in tqdm(files):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as place_info_file:
                    place_details = json.load(place_info_file, encoding='utf-8')
                place, created = Place.objects.get_or_create(
                    title=place_details['title'],
                    description_short=place_details['description_short'],
                    description_long=place_details['description_long'],
                    lng=place_details['coordinates']['lng'],
                    lat=place_details['coordinates']['lat'],
                )
                if not created:
                    continue
                for img_url in place_details['imgs']:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()
                    img = Image.objects.create(place=place)
                    img.img.save('img', ContentFile(img_response.content), save=True)

    def add_arguments(self, parser):
        parser.add_argument(
            'folder',
            nargs=1,
            help='Путь к папке с файлами json, содержащими информацию об местах'
        )
