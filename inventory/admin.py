from django.contrib import admin

from .models import Category, Product, StockMovement, Supplier, Transfer, Warehouse


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(StockMovement)
admin.site.register(Transfer)
