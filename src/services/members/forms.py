from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'phone_number','cnic_number','email','role']
