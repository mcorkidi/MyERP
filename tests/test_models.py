from django.test import TestCase
from core.models import Company


class CompanyModelTest(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(name='Acme', code='ACME')
        self.assertEqual(company.code, 'ACME')
