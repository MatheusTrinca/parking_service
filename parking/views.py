from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from core.permissions import IsOwnerOfVehicleOrRecord
from parking.filters import ParkingRecordFilterClass, ParkingSpotFilterClass
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]
    rql_filter_class = ParkingSpotFilterClass


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]
    rql_filter_class = ParkingRecordFilterClass

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
