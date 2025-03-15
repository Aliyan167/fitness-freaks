from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Fee
from .forms import FeeForm


class FeeListView(ListView):
    model = Fee
    template_name = 'fee-list.html'
    context_object_name = 'fee_list'
    paginate_by = 5  # Set pagination to 5 per page

    from django.db.models import Q

    def get_queryset(self):
        """
        Filter by search query, status, fee type, and due date.
        """
        search_query = self.request.GET.get('search', '')
        status_filter = self.request.GET.get('status', '')
        fee_type_filter = self.request.GET.get('fee_type', '')
        due_date_filter = self.request.GET.get('due_date', '')

        queryset = Fee.objects.all()

        if search_query:
            queryset = queryset.filter(Q(member__full_name__icontains=search_query))

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        if fee_type_filter:
            queryset = queryset.filter(fee_type=fee_type_filter)

        if due_date_filter:
            queryset = queryset.filter(due_date=due_date_filter)

        return queryset.order_by('-created_at')  # Ordered by latest created


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
