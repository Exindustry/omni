from django.contrib import admin
from modules.shipments.models import Shipment


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'creation_date', 'order']
    list_filter = ['name', 'status', 'creation_date', 'order']
    search_fields = ['name', 'status', 'creation_date', 'order']


admin.site.register(Shipment, ShipmentAdmin)
