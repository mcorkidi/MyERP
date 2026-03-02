from django import forms
from .models import Company, Role, SystemSetting


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CompanyForm(BootstrapModelForm):
    class Meta:
        model = Company
        fields = ['name', 'code', 'email']


class RoleForm(BootstrapModelForm):
    class Meta:
        model = Role
        fields = ['name', 'permissions']


class SystemSettingForm(BootstrapModelForm):
    class Meta:
        model = SystemSetting
        fields = ['key', 'value']
