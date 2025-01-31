from django.urls import path
from . import views
from .views import MembershipCreateView, MembershipUpdateView, MembershipDeleteView

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipListView.as_view(), name='membership_list'),
    path('add/', MembershipCreateView.as_view(), name='membership_add'),
    path('<int:pk>/edit/', MembershipUpdateView.as_view(), name='membership_edit'),
    path('<int:pk>/delete/', MembershipDeleteView.as_view(), name='membership_delete'),
]
