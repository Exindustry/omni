from modules.products.serializers import ProductSerializer
from rest_framework import permissions
from rest_framework import viewsets
from modules.products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all().order_by('-creation_date')
    serializer_class = ProductSerializer
