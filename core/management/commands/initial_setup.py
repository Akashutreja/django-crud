# core/management/commands/initial_setup.py
import json
from django.core.management.base import BaseCommand
from core.models import UserData

class Command(BaseCommand):
    help = 'Import location data from a JSON file into the UserData model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

                if not isinstance(data, dict):
                    raise ValueError("Expected a dictionary of user data.")

                # Iterate through each location entry in the JSON
                for key, location_data in data.items():
                    name = location_data.get('name', '')
                    email = location_data.get('email', '')
                    city = location_data.get('city', '')
                    country = location_data.get('country', '')
                    coordinates = location_data.get('coordinates', [None, None])
                    latitude, longitude = coordinates if len(coordinates) == 2 else (None, None)

                    # Check if user with the same email exists
                    user_data = UserData.objects.filter(email=email).first()

                    if user_data:
                        # Update the existing user data if the email exists
                        user_data.name = name
                        user_data.city = city
                        user_data.country = country
                        user_data.coordinates_latitude = latitude
                        user_data.coordinates_longitude = longitude
                        user_data.save()
                        action = "Updated"
                    else:
                        # Create a new user data if the email doesn't exist
                        user_data = UserData.objects.create(
                            name=name,
                            email=email,
                            city=city,
                            country=country,
                            coordinates_latitude=latitude,
                            coordinates_longitude=longitude
                        )
                        action = "Created"

                    self.stdout.write(self.style.SUCCESS(f"{action}: {user_data.name}"))

            self.stdout.write(self.style.SUCCESS('Successfully imported data!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
