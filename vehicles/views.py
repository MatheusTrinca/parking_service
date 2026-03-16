from rest_framework import viewsets

from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer
from vehicles.models import VehicleType, Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer