import os
import django
import requests
import random
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
django.setup()

from rent.models import Customer, Vehicle, RentalStation

BASE_URL = 'http://127.0.0.1:8000/api/rental/'


def create_rentals():
    customer_ids = list(Customer.objects.values_list('id', flat=True))
    vehicle_ids = list(Vehicle.objects.values_list('id', flat=True))
    rental_station_ids = list(RentalStation.objects.values_list('id', flat=True))

    rental_data = {
        "return_date": "2023-08-20",
    }

    for _ in range(200):
        rental_date = datetime(2023, 4, 1) + timedelta(days=random.randint(0, 137))
        rental_data["rental_date"] = rental_date.strftime('%Y-%m-%d')

        rental_data["customer"] = random.choice(customer_ids)
        rental_data["vehicle"] = random.choice(vehicle_ids)
        rental_data["rental_station"] = random.choice(rental_station_ids)

        if random.choice([True, False]):
            rental_data["return_date"] = (rental_date + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')

        response = requests.post(BASE_URL, json=rental_data)

        if response.status_code == 201:
            print(f"Rental created for customer {rental_data['customer']}")
        else:
            print(f"Failed to create rental for customer {rental_data['customer']}: {response.content}")


if __name__ == "__main__":
    create_rentals()
