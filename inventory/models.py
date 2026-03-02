from django.db import models
from common.models import SoftDeleteModel
from core.models import Company


class Category(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


class Supplier(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


class Product(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=80, unique=True)
    quantity_on_hand = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)


class Warehouse(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


class StockMovement(SoftDeleteModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=20)


class Transfer(SoftDeleteModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='out_transfers')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='in_transfers')
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
