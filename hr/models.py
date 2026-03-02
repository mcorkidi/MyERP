from django.db import models
from common.models import SoftDeleteModel
from core.models import Company, User


class Department(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


class Position(SoftDeleteModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)


class Employee(SoftDeleteModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField()


class Attendance(SoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)


class LeaveRequest(SoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='pending')


class Payroll(SoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    period = models.CharField(max_length=20)
    gross = models.DecimalField(max_digits=12, decimal_places=2)
    net = models.DecimalField(max_digits=12, decimal_places=2)
