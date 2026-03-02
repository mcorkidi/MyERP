from django.db import models
from common.models import SoftDeleteModel
from core.models import Company
from inventory.models import Supplier, Product


class PurchaseOrder(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='draft')
    total = models.DecimalField(max_digits=12, decimal_places=2)


class GoodsReceipt(SoftDeleteModel):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)


class VendorBill(SoftDeleteModel):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')


class PurchasePayment(SoftDeleteModel):
    vendor_bill = models.ForeignKey(VendorBill, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
