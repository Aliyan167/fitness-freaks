from datetime import date
from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['user',  'amount', 'discount', 'tax_rate', 'due_date', 'payment_date', 'payment_method', 'status', 'is_paid', 'issue_date', ]

    # Custom validation for amount and due_date
