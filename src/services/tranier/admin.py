from django.contrib import admin
from .models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'specialization', 'experience', 'phone_number')  # Added 'name'
    search_fields = ('name', 'member__membername', 'member__email', 'specialization')  # Added 'name' to search
    list_filter = ('specialization',)
    ordering = ('-experience',)
