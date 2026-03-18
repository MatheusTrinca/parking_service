from django.urls import include, path
from rest_framework import routers

from parking.views import ParkingSpotViewSet, ParkingRecordViewSet

router = routers.DefaultRouter()

router.register(r"parking/spots", ParkingSpotViewSet)
router.register(r"parking/records", ParkingRecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
