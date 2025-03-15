from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member
from django.core.paginator import Paginator

from .. import members
from .forms import MemberForm


class MemberListView(ListView):
    model = Member
    template_name = "members_list.html"
    context_object_name = "members"
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get("search", "")
        queryset = Member.objects.all()

        if search_query:
            queryset = queryset.filter(
                full_name__icontains=search_query
            ) | queryset.filter(
                email__icontains=search_query
            ) | queryset.filter(
                phone_number__icontains=search_query
            )

        return queryset

class MemberDetailView(DetailView):
        model = Member
        template_name = 'member_detail.html'
        context_object_name = 'member'


class MemberCreateView(CreateView):
        model = Member
        form_class = MemberForm
        template_name = 'member_form.html'
        success_url = reverse_lazy('members:members-list')


class MemberUpdateView(UpdateView):
        model = Member
        form_class = MemberForm
        template_name = 'member_update.html'
        success_url = reverse_lazy('members:members-list')


class MemberDeleteView(DeleteView):
        model = Member
        template_name = 'member_confirm_delete.html'
        success_url = reverse_lazy('members:members-list')


