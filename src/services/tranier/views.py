from django.views.generic import TemplateView
from .models import Trainer


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
