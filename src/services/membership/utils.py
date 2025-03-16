from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from src.services.members.models import Member
from src.services.membership.models import Membership


def send_expired_membership_email():
    """
    Checks for expired memberships and sends an email notification
    to the respective members.
    """
    today = timezone.now().date()

    # Get all memberships that have expired
    expired_memberships = Membership.objects.filter(end_date__lt=today, is_active=True)

    for membership in expired_memberships:
        member_email = membership.member.email
        subject = "Your Membership Has Expired"
        message = (
            f"Dear {membership.member},\n\n"
            f"Your {membership.membership_type} membership expired on {membership.end_date.strftime('%B %d, %Y')}."
            f" Please renew your membership to continue enjoying the benefits.\n\n"
            f"Best Regards,\nYour Organization"
        )

        # Send email
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [member_email])

        # Mark membership as inactive after email is sent
        membership.is_active = False
        membership.save()

    return f"Sent {expired_memberships.count()} expiration emails."
