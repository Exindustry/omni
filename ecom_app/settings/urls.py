from django.contrib import admin
from django.urls import path, include
from modules.users.views import api_signin, api_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_in/', api_signin, name='api_sign_in'),
    path('logout/', api_logout, name='api_logout'),
    path('products/', include('modules.products.urls')),
    path('orders/', include('modules.orders.urls')),
    path('payments/', include('modules.payments.urls')),
    path('shipments/', include('modules.shipments.urls')),
]
