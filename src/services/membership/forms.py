from django import forms
from .models import Membership


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['user', 'membership_type', 'end_date', 'is_active']  # Removed 'start_date'
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
