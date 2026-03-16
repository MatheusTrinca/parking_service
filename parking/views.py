from rest_framework import viewsets

from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer
from parking.models import ParkingRecord, ParkingSpot


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer