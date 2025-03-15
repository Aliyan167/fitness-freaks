from django.conf import settings
from django.db import models
from src.services.members.models import Member

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=255)
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='trainers',
    )

    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Trainer: {self.name} - {self.specialization}"


