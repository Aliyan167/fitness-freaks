from django.db.models import Q
from django.views.generic import ListView
from .models import Membership


class MembershipListView(ListView):
    model = Membership
    template_name = 'membership.html'
    context_object_name = 'memberships'  # Name of the context variable
    paginate_by = 10  # Optional pagination: 10 records per page

    def get_queryset(self):
        """
        Fetch membership records and filter them based on search query (username).
        Optionally, order them by the 'start_date' field or 'created_at' field.
        """
        search_query = self.request.GET.get('search', '')  # Get search query from URL parameters
        queryset = Membership.objects.all()  # Start with all memberships

        if search_query:
            # If search query exists, filter memberships based on username
            queryset = queryset.filter(Q(user__username__icontains=search_query))

        # Ensure the list is ordered by 'start_date' or 'created_at' (or another valid field)
        return queryset.order_by('start_date')  # Replace 'start_date' with a valid field in your model

    def get_context_data(self, **kwargs):
        """
        Pass additional context to the template, such as the search query.
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  # Add search query to context for form
        return context
