from django.urls import path
from .views import PurchaseOrderListView

app_name = 'purchase'
urlpatterns = [path('orders/', PurchaseOrderListView.as_view(), name='po_list')]
