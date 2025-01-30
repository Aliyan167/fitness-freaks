from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipListView.as_view(), name='membership_list'),
]
