from datetime import date
from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['member',  'amount', 'discount', 'tax_rate',   'payment_method', 'status', 'is_paid', 'issue_date' ]

    # Custom validation for amount and due_date
