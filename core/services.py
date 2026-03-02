from .models import AuditLog


def log_action(user, action, obj, details=None):
    AuditLog.objects.create(
        actor=user,
        action=action,
        object_type=obj.__class__.__name__,
        object_id=getattr(obj, 'id', None),
        details=details or {},
    )
