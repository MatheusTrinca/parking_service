from rest_framework import permissions

from vehicles.models import Vehicle
from parking.models import ParkingRecord


class IsOwnerOfVehicleOrRecord(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Vehicle):
            return obj.owner.user == request.user
        elif isinstance(obj, ParkingRecord):
            return obj.vehicle.owner.user == request.user
        return False