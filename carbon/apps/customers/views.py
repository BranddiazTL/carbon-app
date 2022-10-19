from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """

    permission_classes = (IsAuthenticated, IsAdminUser)

    queryset = Customer.objects.all().order_by("-created")
    serializer_class = CustomerSerializer
