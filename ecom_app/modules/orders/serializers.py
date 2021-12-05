from rest_framework import serializers
from modules.orders.models import Order, OrderMvto


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', '__str__', 'status', 'created_by', 'creation_date']
        read_only_fields = ['id', 'creation_date']


class OrderMvtoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderMvto
        fields = ['id', '__str__', 'order', 'product', 'cant', 'created_by', 'amount']
        read_only_fields = ['id']
        # depth = 1
