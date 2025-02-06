from django.utils.timezone import now
from django.db.models.functions import TruncMonth
from django.db.models import Count
from src.services.membership.models import Membership
from src.services.fee.models import Fee 
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.db.models.functions import TruncMonth
from django.db.models import Count

User = get_user_model()

def get_users_per_month():
    """Returns a list of user counts per month."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data = {month: 0 for month in months}

    queryset = User.objects.annotate(month=TruncMonth('date_joined')) \
        .values('month').annotate(count=Count('id'))

    for entry in queryset:
        month_name = entry['month'].strftime("%b")
        data[month_name] = entry['count']

    return list(data.values())

def get_memberships_per_month():
    """Returns a list of membership counts per month."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data = {month: 0 for month in months}

    queryset = Membership.objects.annotate(month=TruncMonth('start_date')) \
        .values('month').annotate(count=Count('id'))

    for entry in queryset:
        month_name = entry['month'].strftime("%b")
        data[month_name] = entry['count']

    return list(data.values())

def get_paid_fees_per_month():
    """Returns a list of paid fee instances per month."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data = {month: 0 for month in months}

    queryset = Fee.objects.filter(status='Paid').annotate(month=TruncMonth('payment_date')) \
        .values('month').annotate(count=Count('id'))

    for entry in queryset:
        month_name = entry['month'].strftime("%b")
        data[month_name] = entry['count']

    return list(data.values())
