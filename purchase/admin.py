from django.contrib import admin

from .models import GoodsReceipt, PurchaseOrder, PurchasePayment, VendorBill


admin.site.register(PurchaseOrder)
admin.site.register(GoodsReceipt)
admin.site.register(VendorBill)
admin.site.register(PurchasePayment)
