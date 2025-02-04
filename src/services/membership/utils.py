from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Membership
from datetime import timedelta

def send_membership_expiration_email(user_email, user_name, package_expiry_date):
    subject = "Your Gym Package is About to Expire"
    message = f"Hi {user_name},\n\nYour gym package will expire on {package_expiry_date}. Please renew your package before then.\n\nThanks,\nYour Gym Team"
    from_email = 'your-email@example.com'  # Set your default email here

    # Send the email
    send_mail(subject, message, from_email, [user_email])

def check_and_send_expiration_notifications():
    """Check all memberships and send expiration email if needed."""
    today = now().date()
    # Find memberships expiring in the next 30 days
    memberships = Membership.objects.filter(end_date__lte=today + timedelta(days=30), is_active=True)

    for membership in memberships:
        send_membership_expiration_email(membership.user.email, membership.user.username, membership.end_date)



