from django.core.management.base import BaseCommand
from faker import Faker
from rent.models import Address, Customer, RentalStation, Vehicle, VehicleType, VehicleSize
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument('num_customers', type=int, help='Number of customers to create')
        parser.add_argument('num_stations', type=int, help='Number of rental stations to create')
        parser.add_argument('num_vehicles', type=int, help='Number of vehicles to create')

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Populating the database with sample data...'))

        def create_address():
            return Address.objects.create(
                address=fake.street_address(),
                address2=fake.secondary_address(),
                city=fake.city(),
                country=fake.country(),
                postal_code=fake.postalcode(),
            )

        def create_customer():
            address = create_address()
            while True:
                email = fake.email()
                if not Customer.objects.filter(email=email).exists():
                    break
            return Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                phone_number=fake.phone_number(),
                address=address,
            )

        def create_rental_station():
            address = create_address()
            return RentalStation.objects.create(
                name=fake.street_address(),
                capacity=fake.random_int(min=5, max=50),
                address=address,
            )

        def create_vehicle():
            vehicle_type = random.choice(VehicleType.objects.all())
            vehicle_size = random.choice(VehicleSize.objects.all())
            return Vehicle.objects.create(
                vehicle_type=vehicle_type,
                date_created=fake.date_this_decade(),
                real_cost=random.uniform(20.0, 200.0),
                size=vehicle_size,
            )

        num_customers = kwargs['num_customers']
        num_stations = kwargs['num_stations']
        num_vehicles = kwargs['num_vehicles']

        for _ in range(num_customers):
            create_customer()

        for _ in range(num_stations):
            create_rental_station()

        for _ in range(num_vehicles):
            create_vehicle()

        self.stdout.write(
            self.style.SUCCESS(
                f'{num_customers} customers, {num_stations} rental stations and {num_vehicles} vehicles created successfully.'))
