from rest_framework.permissions import BasePermission


class IsCompanyScoped(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        return getattr(obj, 'company_id', None) == getattr(user, 'company_id', None)
