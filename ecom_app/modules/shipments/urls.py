from django.urls import path, include
from rest_framework import routers
from modules.shipments.views import ShipmentViewSet

router = routers.DefaultRouter()
router.register(r'', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
