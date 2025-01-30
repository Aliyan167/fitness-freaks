from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Fee

@receiver(post_delete, sender=Fee)
def renumber_fees(sender, instance, **kwargs):
    """
    This function is called after a Fee is deleted, to update the IDs of the remaining records.
    """
    # Renumber Fee IDs after deletion (This is not a typical approach, just for your case)
    fees = Fee.objects.all().order_by('created_at')  # You can customize the order
    for idx, fee in enumerate(fees, start=1):
        fee.id = idx  # Set new ID
        fee.save()


