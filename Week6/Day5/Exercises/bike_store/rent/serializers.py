from rest_framework import serializers
from .models import Rental, Customer, Vehicle, RentalStation, VehicleAtRentalStation


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class RentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalStation
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    rental = RentalSerializer(source='vehicleatrentalstation.rental', read_only=True)
    station = RentalStationSerializer(source='vehicleatrentalstation.rental_station', read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAtRentalStation
        fields = '__all__'


class VehicleDistributionStatsSerializer(serializers.Serializer):
    name = serializers.CharField()
    num_vehicles = serializers.IntegerField()
