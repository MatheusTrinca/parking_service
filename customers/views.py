from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions

from customers.serializers import CustomerSerializer
from customers.models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
