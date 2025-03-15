from django.utils import timezone

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from model_utils.models import now
from .models import Membership
from .forms import MembershipForm


class MembershipListView(ListView):
    model = Membership
    paginate_by = 10

    def get_queryset(self):
        """
        Fetch membership records and filter them based on search query (username).
        Optionally, order them by the 'start_date' field or 'created_at' field.
        """
        search_query = self.request.GET.get('search', '')  # Get search query from URL parameters
        queryset = Membership.objects.all()  # Start with all memberships

        if search_query:
            # If search query exists, filter memberships based on username
            queryset = queryset.filter(Q(member__membername__icontains=search_query))

        # Ensure the list is ordered by 'start_date' or 'created_at' (or another valid field)
        return queryset.order_by('start_date')  # Replace 'start_date' with a valid field in your model

    def get_context_data(self, **kwargs):
        """
        Add pagination details to the context.
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  # Add search query to context for form
        return context


class MembershipCreateView(CreateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'membership/membership_form.html'
    success_url = reverse_lazy('membership:membership_list')

    def form_valid(self, form):
        membership = form.save(commit=False)
        membership.start_date = timezone.now().date()  # Set the date
        membership.save()
        return super().form_valid(form)




class MembershipUpdateView(UpdateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'membership/membership_form.html'
    success_url = reverse_lazy('membership:membership_list')



class MembershipDeleteView(DeleteView):
    model = Membership
    template_name = 'membership/membership_confirm_delete.html'
    success_url = reverse_lazy('membership:membership_list')
