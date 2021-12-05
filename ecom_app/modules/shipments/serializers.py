from rest_framework import serializers
from modules.shipments.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
        read_only_fields = ['id', 'creation_date', 'consecutive', 'shipment_date', 'received_date']
