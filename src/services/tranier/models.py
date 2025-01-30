from django.conf import settings
from django.db import models

# Create your models here.
class Trainer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trainer_profile'
    )
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Trainer: {self.user.username} - {self.specialization}"


