from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CompanySerializer, EmployeeSerializer, ProductSerializer,
    SalesOrderSerializer, PurchaseOrderSerializer, JournalEntrySerializer
)
from .permissions import IsCompanyScoped
from core.models import Company
from hr.models import Employee
from inventory.models import Product
from sales.models import SalesOrder
from purchase.models import PurchaseOrder
from accounting.models import JournalEntry


class BaseScopedViewSet(ModelViewSet):
    permission_classes = [IsCompanyScoped]

    def get_queryset(self):
        qs = super().get_queryset().filter(is_deleted=False)
        if self.request.user.is_superuser:
            return qs
        company_id = getattr(self.request.user, 'company_id', None)
        return qs.filter(company_id=company_id) if hasattr(self.queryset.model, 'company_id') else qs


class CompanyViewSet(BaseScopedViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_fields = ['name', 'code']
    search_fields = ['name', 'code']


class EmployeeViewSet(BaseScopedViewSet):
    queryset = Employee.objects.select_related('company', 'user').all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['company', 'department']
    search_fields = ['user__username']


class ProductViewSet(BaseScopedViewSet):
    queryset = Product.objects.select_related('company').all()
    serializer_class = ProductSerializer
    filterset_fields = ['company', 'category']
    search_fields = ['name', 'sku']


class SalesOrderViewSet(BaseScopedViewSet):
    queryset = SalesOrder.objects.select_related('customer').all()
    serializer_class = SalesOrderSerializer


class PurchaseOrderViewSet(BaseScopedViewSet):
    queryset = PurchaseOrder.objects.select_related('company', 'supplier').all()
    serializer_class = PurchaseOrderSerializer


class JournalEntryViewSet(BaseScopedViewSet):
    queryset = JournalEntry.objects.select_related('company').all()
    serializer_class = JournalEntrySerializer
