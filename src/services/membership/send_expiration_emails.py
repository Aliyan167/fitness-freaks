from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from src.services.membership.models import Membership

class Command(BaseCommand):
    help = "Send expiration emails to members whose membership is expiring soon."

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        expiration_threshold = today + timezone.timedelta(days=30)

        memberships_to_notify = Membership.objects.filter(
            expiration_date__lte=expiration_threshold, expiration_date__gt=today
        )

        for membership in memberships_to_notify:
            subject = "Your Membership is About to Expire"
            message = (
                f"Dear {membership.member},\n\n"
                f"Your membership will expire on {membership.expiration_date.strftime('%B %d, %Y')}."
                f" Please renew your membership to continue enjoying the benefits."
            )
            recipient_list = [membership.member.email]

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        self.stdout.write(self.style.SUCCESS(f"Sent {memberships_to_notify.count()} expiration emails."))
