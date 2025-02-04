
from django.urls import path
from .views import TrainerListView , TrainerCreateView, TrainerUpdateView, TrainerDeleteView

app_name = "tranier"

urlpatterns = [
    path('', TrainerListView.as_view(), name='trainer_list'),
    path("add/", TrainerCreateView.as_view(), name="trainer_add"),
    path("<int:pk>/edit/", TrainerUpdateView.as_view(), name="trainer_edit"),
    path("<int:pk>/delete/", TrainerDeleteView.as_view(), name="trainer_delete")
    ]



