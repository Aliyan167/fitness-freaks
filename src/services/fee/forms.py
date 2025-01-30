from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = [
            'user', 'order', 'amount', 'discount', 'tax_rate', 'due_date',
            'payment_date', 'payment_method', 'status', 'is_paid', 'issue_date',
            'total_amount'
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }