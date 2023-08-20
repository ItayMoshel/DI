from django.core.management.base import BaseCommand
from rent.models import VehicleType, VehicleSize


class Command(BaseCommand):
    help = 'Repopulate VehicleType and VehicleSize data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Repopulating VehicleType and VehicleSize data...'))

        # Clear existing data
        VehicleType.objects.all().delete()
        VehicleSize.objects.all().delete()

        # Repopulate VehicleType
        VehicleType.objects.create(name='Scooter')
        VehicleType.objects.create(name='Bicycle')
        # Add more vehicle types if needed

        # Repopulate VehicleSize
        VehicleSize.objects.create(name='Small')
        VehicleSize.objects.create(name='Medium')
        # Add more vehicle sizes if needed

        self.stdout.write(self.style.SUCCESS('VehicleType and VehicleSize data repopulated successfully.'))
