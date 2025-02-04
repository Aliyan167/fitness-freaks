from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Fee
from .forms import FeeForm


class FeeListView(ListView):
    model = Fee
    template_name = 'fee-list.html'
    context_object_name = 'fee_list'
    paginate_by = 5  # Set pagination to 10 per page

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




class FeeCreateView(CreateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fee_form.html'
    success_url = reverse_lazy('fee:fee_list')




class FeeUpdateView(UpdateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fee_update.html'
    success_url = reverse_lazy('fee:fee_list')


# DeleteView for deleting a fee record

class FeeDeleteView(DeleteView):
    model = Fee
    template_name = 'fee_confirm_delete.html'
    success_url = reverse_lazy('fee:fee_list')
