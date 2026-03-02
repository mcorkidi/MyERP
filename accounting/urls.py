from django.urls import path
from .views import JournalEntryListView

app_name = 'accounting'
urlpatterns = [path('journals/', JournalEntryListView.as_view(), name='journal_list')]
