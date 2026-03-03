from django.contrib import admin

from .models import Attendance, Department, Employee, LeaveRequest, Payroll, Position


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
admin.site.register(Payroll)
