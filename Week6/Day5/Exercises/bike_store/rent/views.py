from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rental, Customer, Vehicle, RentalStation
from .serializers import (RentalSerializer,
                          CustomerSerializer,
                          VehicleSerializer,
                          RentalStationSerializer,
                          VehicleDistributionStatsSerializer,
                          VehicleAtRentalStation,

                          )
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from django.db.models import Count, Case, When, F, Value, IntegerField


class RentalListCreateAPIView(APIView):
    def get(self, request):
        rentals = Rental.objects.order_by('return_date', 'rental_date')
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalDetailAPIView(APIView):
    def get(self, request, pk):
        rental = get_object_or_404(Rental, pk=pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data)

    def put(self, request, pk):
        rental = get_object_or_404(Rental, pk=pk)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rental = get_object_or_404(Rental, pk=pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerListAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.prefetch_related('rental_set').order_by('last_name', 'first_name')
        customer_data = []

        for customer in customers:
            rental_info = None
            if customer.rental_set.exists():
                latest_rental = customer.rental_set.latest('rental_date')
                rental_info = {
                    'is_renting': True,
                    'rental_id': latest_rental.id,
                }

            customer_data.append({
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email,
                'phone_number': customer.phone_number,
                'is_renting': rental_info['is_renting'] if rental_info else False,
                'rental_id': rental_info['rental_id'] if rental_info else None,
            })

        return Response(customer_data, status=status.HTTP_200_OK)


class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        rental_info = None
        if instance.rental_set.exists():
            latest_rental = instance.rental_set.latest('rental_date')
            rental_info = {
                'is_renting': True,
                'rental_id': latest_rental.id,
            }

        data = serializer.data
        data['is_renting'] = rental_info['is_renting'] if rental_info else False
        data['rental_id'] = rental_info['rental_id'] if rental_info else None

        return Response(data)


class CustomerAddAPIView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleListAPIView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


class VehicleDetailAPIView(APIView):
    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleAddAPIView(APIView):
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalStationListAPIView(APIView):
    def get(self, request):
        rental_stations = RentalStation.objects.all()
        serializer = RentalStationSerializer(rental_stations, many=True)
        return Response(serializer.data)


class RentalStationAddAPIView(APIView):
    def post(self, request):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalStationDetailAPIView(APIView):
    def get(self, request, station_id):
        rental_station = get_object_or_404(RentalStation, id=station_id)
        serializer = RentalStationSerializer(rental_station)
        return Response(serializer.data)


class VehicleDistributionStatsAPIView(APIView):
    def get(self, request):
        distribution_stats = RentalStation.objects.annotate(num_vehicles=Count('vehicleatrentalstation')).values('name',
                                                                                                                 'num_vehicles')
        serializer = VehicleDistributionStatsSerializer(distribution_stats, many=True)
        return Response(serializer.data)


class VehicleDistributionAPIView(APIView):
    def post(self, request):
        try:
            total_stations = RentalStation.objects.count()
            total_vehicles = Vehicle.objects.count()
            vehicles_per_station = total_vehicles // total_stations
            stations = RentalStation.objects.all()
            vehicles = list(Vehicle.objects.all())

            for station in stations:
                station_vehicles = vehicles[:vehicles_per_station]
                for vehicle in station_vehicles:
                    VehicleAtRentalStation.objects.create(
                        vehicle=vehicle,
                        rental_station=station,
                        arrival_date=timezone.now()  # Set the arrival_date to current time
                    )
                vehicles = vehicles[vehicles_per_station:]

            return Response({'message': 'Vehicles successfully distributed among stations.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MonthlyRentalStatsAPIView(APIView):
    def get(self, request):
        try:
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')

            rentals = Rental.objects.all()
            if start_date:
                rentals = rentals.filter(rental_date__gte=start_date)
            if end_date:
                rentals = rentals.filter(rental_date__lte=end_date)

            monthly_stats = rentals.annotate(month=TruncMonth('rental_date')) \
                .values('month') \
                .annotate(total_rentals=Count('id')) \
                .annotate(bike_rentals=Count(
                Case(When(vehicle__vehicle_type__name='Motorcycle', then=Value(1)), output_field=IntegerField())
            )) \
                .annotate(scooter_rentals=Count(
                Case(When(vehicle__vehicle_type__name='Scooter', then=Value(1)), output_field=IntegerField())
            ))

            response_data = []
            for item in monthly_stats:
                month_str = item['month'].strftime('%Y-%m')
                data = {
                    'month': month_str,
                    'total_rentals': item['total_rentals'],
                    'bike_rentals': item['bike_rentals'],
                    'scooter_rentals': item['scooter_rentals'],
                }
                response_data.append(data)

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PopularRentalStationStatsAPIView(APIView):
    def get(self, request):
        try:
            rental_station_stats = RentalStation.objects.annotate(total_rentals=Count('vehicleatrentalstation__rental')) \
                .order_by('-total_rentals') \
                .values('name', 'total_rentals')

            print(rental_station_stats.query)  # This will print the generated SQL query

            response_data = []
            for item in rental_station_stats:
                data = {
                    'station_name': item['name'],
                    'total_rentals': item['total_rentals'],
                }
                response_data.append(data)

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MostRentedVehicleTypeAPIView(APIView):
    def get(self, request):
        try:
            vehicle_type_stats = Vehicle.objects.values('vehicle_type__name') \
                .annotate(total_rentals=Count('rental')) \
                .order_by('-total_rentals')

            response_data = {}
            for item in vehicle_type_stats:
                vehicle_type = item['vehicle_type__name']
                total_rentals = item['total_rentals']
                response_data[vehicle_type] = total_rentals

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
