from django.urls import include, path
from rest_framework import routers
from modules.orders.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
