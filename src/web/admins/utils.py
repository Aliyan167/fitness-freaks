from django.utils.timezone import now
from django.db.models.functions import TruncMonth
from django.db.models import Count
from src.services.membership.models import Membership
from src.services.fee.models import Fee 
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.db.models import Count
from datetime import datetime, timedelta
from src.services.members.models import Member

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

def get_users_per_day():
    """Returns a list of user counts per day for the current month and year."""
    today = datetime.today()
    year, month = today.year, today.month

    # Get total days in the current month
    next_month = month % 12 + 1
    next_month_year = year if next_month > 1 else year + 1
    days_in_month = (datetime(next_month_year, next_month, 1) - timedelta(days=1)).day

    data = {day: 0 for day in range(1, days_in_month + 1)}

    queryset = User.objects.filter(date_joined__year=year, date_joined__month=month) \
        .annotate(day=TruncDay('date_joined')) \
        .values('day') \
        .annotate(count=Count('id'))

    for entry in queryset:
        day_num = entry['day'].day
        data[day_num] = entry['count']

    return list(data.values())
