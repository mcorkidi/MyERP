from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from common.models import SoftDeleteModel


class Company(SoftDeleteModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)

    class Meta:
        indexes = [models.Index(fields=['code'])]

    def __str__(self):
        return self.name


class Role(SoftDeleteModel):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)


class AuditLog(SoftDeleteModel):
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=120)
    object_type = models.CharField(max_length=120)
    object_id = models.UUIDField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)


class SystemSetting(SoftDeleteModel):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
