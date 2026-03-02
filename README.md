# MyERP (Django + DRF + Templates)

## Project Structure
- `config/`: project settings, urls, wsgi/asgi.
- `common/`: base UUID + soft delete models.
- `core/`: users, company tenancy, roles, audit logs, settings.
- `hr/`, `inventory/`, `sales/`, `purchase/`, `accounting/`, `reports/`: ERP modules.
- `api/`: DRF serializers, viewsets, permissions.
- `templates/`: complete template layout and module CRUD templates.

## Database Schema (High-level)
- Tenant root is `core.Company`.
- `core.User` belongs to `Company` and `Role`.
- Operational modules (HR, Inventory, Sales, Purchase, Accounting) connect to `Company` and cross-link through FK relations.
- All entities use UUID PK and `is_deleted` soft-delete flag.

## Deployment
1. Set env vars: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `POSTGRES_*`.
2. Install dependencies: Django, djangorestframework, drf-spectacular, django-filter, psycopg2-binary.
3. Run migrations and collectstatic.
4. Serve with Gunicorn + Nginx.
5. Enable HTTPS and configure proper `ALLOWED_HOSTS`.

## API Docs
- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/docs/`

## Notes
- Service layer examples in `core/services.py`, `sales/services.py`, `accounting/services.py`.
- Role-based sidebar visibility in `templates/components/sidebar.html`.
- Reporting template pages in `templates/reports/`.
