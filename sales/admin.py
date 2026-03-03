from django.contrib import admin

from .models import Customer, Invoice, Payment, Quotation, SalesOrder, TaxRate


admin.site.register(Customer)
admin.site.register(Quotation)
admin.site.register(SalesOrder)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(TaxRate)
