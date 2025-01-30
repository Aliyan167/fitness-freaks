from django.views.generic import ListView
from django.db.models import Q
from .models import Attendance

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendence.html'
    context_object_name = 'attendances'  # Fixed typo
    paginate_by = 10  # Display 10 records per page

    def get_queryset(self):
        """
        Fetch attendance records and filter them based on search query (username).
        Ensures the correct ordering of the records by 'created_at' field.
        """
        search_query = self.request.GET.get('search', '')
        queryset = Attendance.objects.select_related('user').order_by('created_at')  # Correct ordering to ascending

        if search_query:
            queryset = queryset.filter(Q(user__username__icontains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        """
        Pass additional context to the template, such as the search query.
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context
