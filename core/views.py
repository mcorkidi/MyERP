from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


class CompanyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Company
    template_name = 'core/list.html'
    paginate_by = 10
    permission_required = 'core.view_company'


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'core/create.html'
    success_url = reverse_lazy('core:company_list')
    permission_required = 'core.add_company'


class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'core/update.html'
    success_url = reverse_lazy('core:company_list')
    permission_required = 'core.change_company'


class CompanyDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Company
    template_name = 'core/detail.html'
    permission_required = 'core.view_company'


class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Company
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('core:company_list')
    permission_required = 'core.delete_company'
