from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Trainer
from .forms import TrainerForm

class TrainerListView(ListView):  # ✅ Use ListView instead of TemplateView
    model = Trainer
    template_name = "tranier/trainer.html"
    context_object_name = "object_list"  # ✅ Now matches the template

    def get_queryset(self):
        search_query = self.request.GET.get("search", "")
        if search_query:
            return Trainer.objects.filter(member__membername__icontains=search_query)
        return Trainer.objects.all()

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "tranier/trainer_form.html"
    success_url = reverse_lazy("tranier:trainer_list")

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "tranier/trainer_form.html"
    success_url = reverse_lazy("tranier:trainer_list")

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = "tranier/trainer_confirm_delete.html"
    success_url = reverse_lazy("tranier:trainer_list")
