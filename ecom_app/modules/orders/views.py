from modules.orders.serializers import OrderSerializer, OrderMvtoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from modules.orders.models import Order, OrderMvto
from modules.products.models import Product


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('-creation_date')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post', 'get'])
    def create_order_mvto(self, request, pk=None):

        self.serializer_class = OrderMvtoSerializer
        order = self.get_object()
        data = request.data.copy()
        cant = data.get('cant') if data.get('cant') else 1
        product = Product.objects.filter(id=data.get('product')).first()
        product_price = product.price if product else 0
        data['amount'] = product_price * float(cant)
        data['order'] = order.id
        serializer = OrderMvtoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def list_order_mvto(self, request, pk=None):

        self.serializer_class = OrderMvtoSerializer
        order = self.get_object()
        order_mvtos = OrderMvto.objects.filter(order=order)
        page = self.paginate_queryset(order_mvtos)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(order_mvtos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
