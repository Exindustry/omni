from django.contrib import admin
from modules.products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'price']
    list_filter = ['name', 'category', 'description']
    search_fields = ['name', 'category', 'description']


admin.site.register(Product, ProductAdmin)
