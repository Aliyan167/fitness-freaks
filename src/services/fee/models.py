from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from src.services.members.models import Member


class Fee(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
        ('Paid', 'Paid'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
        ('Other', 'Other'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='fees',
    )
    order = models.PositiveIntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
    )
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    issue_date = models.DateField(default=now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # Removed '-due_date'
        verbose_name = 'Fee'
        verbose_name_plural = 'Fees'

    def __str__(self):
        return f"Fee for {self.member.user.username} - Status: {self.status}"

    @property
    def total_amount_due(self):
        """
        Calculate the total amount due after applying discount and tax.
        """
        return self.amount - self.discount + (self.amount * self.tax_rate / 100)

    def clean(self):
        """
        Custom validation to ensure data consistency.
        """
        if self.is_paid and self.status != 'Paid':
            self.status = 'Paid'

        if self.status == 'Paid' and not self.payment_date:
            self.payment_date = now().date()

    def save(self, *args, **kwargs):
        """
        Override save method to auto-update statuses and calculate the total amount.
        """
        # Auto-set payment date if marked as paid
        if self.is_paid and self.payment_date is None:
            self.payment_date = now().date()

        # Calculate total amount if not already provided
        if not self.total_amount:
            self.total_amount = self.total_amount_due

        super().save(*args, **kwargs)

    def mark_as_paid(self, payment_method=None):
        """
        Mark the fee as paid and set payment details.
        """
        self.is_paid = True
        self.status = 'Paid'
        self.payment_date = now().date()
        if payment_method:
            self.payment_method = payment_method
        self.save()
