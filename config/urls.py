from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from api.viewsets import (
    CompanyViewSet, EmployeeViewSet, ProductViewSet, SalesOrderViewSet,
    PurchaseOrderViewSet, JournalEntryViewSet
)
from core.views import DashboardView

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('employees', EmployeeViewSet)
router.register('products', ProductViewSet)
router.register('sales-orders', SalesOrderViewSet)
router.register('purchase-orders', PurchaseOrderViewSet)
router.register('journal-entries', JournalEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include(router.urls)),
    path('core/', include('core.urls')),
    path('hr/', include('hr.urls')),
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
    path('purchase/', include('purchase.urls')),
    path('accounting/', include('accounting.urls')),
    path('reports/', include('reports.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
