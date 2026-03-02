from django.db import models
from common.models import SoftDeleteModel
from core.models import Company


class Customer(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)


class Quotation(SoftDeleteModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='draft')


class SalesOrder(SoftDeleteModel):
    quotation = models.ForeignKey(Quotation, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')


class Invoice(SoftDeleteModel):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    number = models.CharField(max_length=80, unique=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    is_posted = models.BooleanField(default=False)


class Payment(SoftDeleteModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')


class TaxRate(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
