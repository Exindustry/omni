from modules.shipments.serializers import ShipmentSerializer
from rest_framework import permissions
from rest_framework import viewsets
from modules.shipments.models import Shipment


class ShipmentViewSet(viewsets.ModelViewSet):
    
    queryset = Shipment.objects.all().order_by('-creation_date')
    serializer_class = ShipmentSerializer
