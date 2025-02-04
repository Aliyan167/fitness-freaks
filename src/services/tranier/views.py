from django.views.generic import TemplateView
from .models import Trainer
from django.views.generic import  CreateView, UpdateView, DeleteView
from .forms import TrainerForm
from django.urls import reverse_lazy

class TrainerListView(TemplateView):
    template_name = 'trainer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the search query from the GET request
        search_query = self.request.GET.get('search', '')

        # Filter trainers based on the search query
        if search_query:
            trainers = Trainer.objects.filter(user__username__icontains=search_query)
        else:
            trainers = Trainer.objects.all()

        context['trainers'] = trainers
        context['search_query'] = search_query
        return context



class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "trainer_form.html"
    success_url = reverse_lazy("tranier:trainer_list")

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "trainer_form.html"
    success_url = reverse_lazy("tranier:trainer_list")

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = "trainer_confirm_delete.html"
    success_url = reverse_lazy("tranier:trainer_list")