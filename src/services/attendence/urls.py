
from django.urls import path
from .views import AttendanceListView

app_name = 'attendence'

urlpatterns = [
    path('',AttendanceListView.as_view(), name='attendance_detail'),

    ]
