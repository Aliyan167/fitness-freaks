from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from model_utils.models import now
from src.services.members.models import Member



class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, default='Basic')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member} - {self.membership_type}"

    def renew_membership(self, months=1):
        """Extend membership by given months."""
        self.end_date += timedelta(days=30 * months)
        self.save()

    def has_expired(self):
        """Check if membership has expired and update is_active."""
        if self.end_date < timezone.now().date():
            self.is_active = False  # Mark as inactive
            self.save()
        return not self.is_active



