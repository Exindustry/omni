from rest_framework import serializers
from modules.payments.models import Payment, PaymentMvto


class PaymentSerializer(serializers.ModelSerializer):

    orders = serializers.StringRelatedField(many=True)

    class Meta:
        model = Payment
        fields = ['id', '__str__', 'name', 'amount', 'created_by', 'creation_date', 'orders']
        read_only_fields = ['id', 'creation_date']
        depth = 1

class PaymentMvtoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMvto
        fields = ['id', '__str__', 'order', 'payment', 'creation_date', 'amount']
        read_only_fields = ['id', 'creation_date']