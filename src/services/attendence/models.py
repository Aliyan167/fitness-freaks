from django.conf import settings
from django.db import models
from model_utils.models import now


# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendance_records'
    )
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.check_in.strftime('%Y-%m-%d %H:%M')}"

    def mark_checkout(self):
        """Mark user checkout."""
        self.check_out = now()
        self.save()





