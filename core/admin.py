from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import AuditLog, Company, Role, SystemSetting, User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('ERP Access', {'fields': ('company', 'role')}),
    )
    list_display = DjangoUserAdmin.list_display + ('company', 'role')


admin.site.register(Company)
admin.site.register(Role)
admin.site.register(AuditLog)
admin.site.register(SystemSetting)
