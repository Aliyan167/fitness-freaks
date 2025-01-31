from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings


class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='membership'
    )
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, default='Basic')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership_type}"

    def renew_membership(self, months=1):
        """Extend membership by given months."""
        self.end_date += timedelta(days=30 * months)
        self.save()

    def has_expired(self):
        """Check if membership has expired."""
        return now().date() > self.end_date



