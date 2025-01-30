
from django.urls import path
from .views import TrainerListView

app_name = "tranier"

urlpatterns = [
    path('', TrainerListView.as_view(), name='trainer_list'),
    ]