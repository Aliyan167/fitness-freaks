from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from src.services.users.models import User


# Create your views here.
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'phone_number', 'profile_image']
    success_url = reverse_lazy('admins:user-list')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('admins:user-list')
