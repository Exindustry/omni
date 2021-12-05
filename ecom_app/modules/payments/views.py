from modules.payments.serializers import PaymentSerializer, PaymentMvtoSerializer
from rest_framework import viewsets, status
from modules.payments.models import Payment, PaymentMvto
from modules.orders.models import Order
from rest_framework.response import Response
from rest_framework.decorators import action
import json


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-creation_date')
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        new_payment = Payment.objects.create(amount=data.get(
            'amount'), created_by_id=data.get('created_by'), name=data.get('name'))
        new_payment.save()
        
        for order in data.get("orders"):
            order_obj = Order.objects.get(id=order.get("order"))
            order['order'] = order_obj
            PaymentMvto.objects.create(**order, payment=new_payment)

        serializer = PaymentSerializer(new_payment)

        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):

        data = request.data
        data_copy = data.copy()
        del data_copy['orders']
        payment = Payment.objects.filter(id=pk)
        payment_mod = payment.first()
        payment.update(**data_copy)

        for row in data.get('orders'):
            mvto_id = row.get('id')
            del row['id']
            payment_mod.paymentmvto_set.filter(id=mvto_id).update(**row)

        serializer = PaymentSerializer(payment_mod)

        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def add_payment_mvto(self, request, pk=None):

        self.serializer_class = PaymentMvtoSerializer
        payment = self.get_object()
        data = request.data.copy()
        serializer = PaymentMvtoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'])
    def list_payment_mvto(self, request, pk=None):

        data = request.data.copy()
        kwargs_dict = {}

        for key, value in data.items():
            kwargs_dict[key] = value

        if pk:
            kwargs_dict['payment_id'] = pk

        self.serializer_class = PaymentMvtoSerializer
        payment = self.get_object()
        payment_mvtos = PaymentMvto.objects.filter(**kwargs_dict)
        page = self.paginate_queryset(payment_mvtos)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(payment_mvtos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
