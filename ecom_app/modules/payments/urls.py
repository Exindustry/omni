from django.urls import include, path
from rest_framework import routers
from modules.orders.views import OrderViewSet
from modules.payments.views import PaymentViewSet

router = routers.DefaultRouter()
router.register(r'', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
