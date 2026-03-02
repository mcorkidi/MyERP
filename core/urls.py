from django.urls import path
from .views import (
    CompanyListView, CompanyCreateView, CompanyUpdateView,
    CompanyDetailView, CompanyDeleteView
)

app_name = 'core'

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company_create'),
    path('companies/<uuid:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<uuid:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<uuid:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
]
