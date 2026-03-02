from django import forms
from .models import SalesOrder


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['quotation', 'customer', 'total', 'status']
