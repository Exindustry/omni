from rest_framework.authtoken.models import TokenProxy
from modules.payments.models import Payment, PaymentMvto
from django.contrib import admin


class PaymentMvtoTabularInline(admin.TabularInline):
    model = PaymentMvto
    extra = 1


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'amount', 'creation_date']
    list_filter = ['creation_date', 'created_by']
    search_fields = ['creation_date', 'created_by']
    inlines = [PaymentMvtoTabularInline]


admin.site.register(Payment, PaymentModelAdmin)