from django.urls import path
from .views import *

app_name = 'sales'
urlpatterns = [
    path('orders/', SalesOrderListView.as_view(), name='salesorder_list'),
    path('orders/create/', SalesOrderCreateView.as_view(), name='salesorder_create'),
    path('orders/<uuid:pk>/', SalesOrderDetailView.as_view(), name='salesorder_detail'),
    path('orders/<uuid:pk>/update/', SalesOrderUpdateView.as_view(), name='salesorder_update'),
    path('orders/<uuid:pk>/delete/', SalesOrderDeleteView.as_view(), name='salesorder_delete'),
]
