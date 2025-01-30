from django.contrib import admin
from model_utils.models import now

from .models import Membership

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_type', 'start_date', 'end_date', 'is_active')
    list_filter = ('membership_type', 'is_active', 'start_date', 'end_date')
    search_fields = ('user__username',)
    readonly_fields = ('start_date',)

    def has_expired(self, obj):
        return obj.end_date < now().date()
    has_expired.boolean = True
    has_expired.short_description = 'Expired'
