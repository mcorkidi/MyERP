from django.db import models
from common.models import SoftDeleteModel
from core.models import Company


class Account(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=20)


class JournalEntry(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    memo = models.CharField(max_length=255, blank=True)
    posted = models.BooleanField(default=False)


class JournalLine(SoftDeleteModel):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
