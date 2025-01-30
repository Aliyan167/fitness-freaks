from django.urls import path
from .views import FeeListView,FeeDetailView

app_name = "fee"

urlpatterns = [
    path('', FeeListView.as_view(), name='fee_list'),
    path('<int:pk>/', FeeDetailView.as_view(), name='fee_details'),


]
