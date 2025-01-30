from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Fee


class FeeListView(ListView):
    model = Fee
    template_name = 'fee-list.html'
    context_object_name = 'fee_list'
    paginate_by = 10  # Set pagination to 10 per page

    def get_queryset(self):
        """
        Optionally filter by search query and order by the 'order' field or 'created_at'.
        """
        search_query = self.request.GET.get('search', '')
        queryset = Fee.objects.all()

        if search_query:
            queryset = queryset.filter(Q(user__username__icontains=search_query))

        # Ensure the list is ordered by the 'order' field or any other field you want.
        return queryset.order_by('order')  # Or 'created_at' if you prefer it to be in chronological order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  # Add search query to context
        return context


class FeeDetailView(DetailView):
    model = Fee
    template_name = 'fee-details.html'
    context_object_name = 'fee'


