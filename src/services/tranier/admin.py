from django.contrib import admin
from .models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience', 'phone_number')
    search_fields = ('user__username', 'user__email', 'specialization')
    list_filter = ('specialization',)
    ordering = ('-experience',)
