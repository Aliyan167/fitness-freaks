from django.contrib import admin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    """
    Admin interface for the Fee model.
    """
    list_display = (
        'member', 'order', 'amount', 'discount', 'tax_rate', 'total_amount', 'status',
        'is_paid', 'payment_date', 'created_at'
    )
    list_filter = (
        'status', 'is_paid', 'payment_date', 'created_at', 'order'
    )
    search_fields = ('member__membername', 'member__email', 'status', 'order')

    ordering = ('created_at',)
    readonly_fields = ('created_at', 'updated_at', 'total_amount')

    fieldsets = (
        ("Fee Information", {
            'fields': ('member', 'order', 'amount', 'discount', 'tax_rate', 'total_amount', 'status', 'is_paid')
        }),
        ("Dates", {
            'fields': ('issue_date', 'payment_date', 'created_at', 'updated_at')
        }),
        ("Payment Details", {
            'fields': ('payment_method',)
        }),
    )

    def get_queryset(self, request):
        """
        Optimize the queryset to prefetch related fields for better performance.
        """
        queryset = super().get_queryset(request)
        return queryset.select_related('member')

    def get_form(self, request, obj=None, **kwargs):
        """
        Override the form to prepopulate the 'order' field when creating a new Fee.
        """
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Only prepopulate for new Fee entries
            form.base_fields['order'].initial = self.get_next_order_value()
        return form

    def get_next_order_value(self):
        """
        Return the next available 'order' value based on existing records.
        """
        last_fee = Fee.objects.all().order_by('-order').first()
        return last_fee.order + 1 if last_fee else 1
