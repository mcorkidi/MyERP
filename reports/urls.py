from django.urls import path
from .views import *

app_name = 'reports'
urlpatterns = [
    path('sales/', SalesReportView.as_view(), name='sales_report'),
    path('inventory/', InventoryValuationView.as_view(), name='inventory_valuation'),
    path('profit-loss/', ProfitLossView.as_view(), name='profit_loss'),
    path('payroll/', PayrollSummaryView.as_view(), name='payroll_summary'),
]
