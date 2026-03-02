from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SalesReportView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/sales_report.html'


class InventoryValuationView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/inventory_valuation.html'


class ProfitLossView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/profit_loss.html'


class PayrollSummaryView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/payroll_summary.html'
