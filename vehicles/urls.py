from django.urls import include, path
from rest_framework import routers

from vehicles.views import VehicleTypeViewSet, VehicleViewSet

router = routers.DefaultRouter()

router.register(r"vehicles/types", VehicleTypeViewSet)
router.register(r"vehicles", VehicleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
