from django.urls import path

from src.services.users.views import UserCreateView, UserDeleteView
app_name = 'users'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('delete/<str:pk>/', UserDeleteView.as_view(), name='user-delete'),

]