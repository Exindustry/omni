from modules.orders.models import Order, OrderMvto
from django.contrib import admin


class OrderMvtoTabularInline(admin.TabularInline):
    model = OrderMvto
    extra = 1


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'status', 'creation_date']
    list_filter = ['creation_date', 'status', 'created_by']
    search_fields = ['creation_date', 'status', 'created_by']
    inlines = [OrderMvtoTabularInline]


admin.site.register(Order, OrderModelAdmin)