from django.urls import path
from .views import FeeListView, FeeDetailView, FeeCreateView, FeeUpdateView, FeeDeleteView

app_name = "fee"

urlpatterns = [
    path('', FeeListView.as_view(), name='fee_list'),
    path('<int:pk>/', FeeDetailView.as_view(), name='fee_details'),
    path('create/', FeeCreateView.as_view(), name='fee_create'),
    path('<int:pk>/update/', FeeUpdateView.as_view(), name='fee_update'),
    path('<int:pk>/delete/', FeeDeleteView.as_view(), name='fee_delete'),
]
