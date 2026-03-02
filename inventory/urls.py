from django.urls import path
from .views import *

app_name = 'inventory'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<uuid:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
