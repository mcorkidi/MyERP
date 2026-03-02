from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import PurchaseOrder


class PurchaseOrderListView(LoginRequiredMixin, ListView):
    model = PurchaseOrder
    template_name = 'purchase/list.html'
    paginate_by = 10
