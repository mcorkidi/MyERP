from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import JournalEntry


class JournalEntryListView(LoginRequiredMixin, ListView):
    model = JournalEntry
    template_name = 'accounting/list.html'
    paginate_by = 10
