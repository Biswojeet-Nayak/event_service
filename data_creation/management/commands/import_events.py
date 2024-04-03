import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from data_creation.models import Event  # Importing the Event model from the data_creation app


class Command(BaseCommand):
    help = 'Import events from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                event = Event(
                    event_name=row['event_name'],
                    city_name=row['city_name'],
                    date=datetime.strptime(row['date'], '%Y-%m-%d').date(),
                    time=datetime.strptime(row['time'], '%H:%M:%S').time(),
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude'])
                )
                event.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported events from CSV file.'))
