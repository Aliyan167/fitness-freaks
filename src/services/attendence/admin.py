from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def has_change_permission(self, request, obj=None):
        """Restrict the ability to edit check-out time"""
        if obj and obj.check_out is not None:
            return False
        return super().has_change_permission(request, obj)

admin.site.register(Attendance, AttendanceAdmin)
