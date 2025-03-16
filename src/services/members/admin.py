from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'cnic_number', 'role', 'joined_at')
    search_fields = ('full_name', 'email', 'phone_number', 'cnic_number')
    list_filter = ('role', 'joined_at')
    ordering = ('-joined_at',)