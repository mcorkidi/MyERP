from django.urls import path
from .views import *

app_name = 'hr'
urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<uuid:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<uuid:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<uuid:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
