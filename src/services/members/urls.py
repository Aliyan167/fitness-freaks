from django.urls import path
from .views import MemberListView,MemberDetailView,MemberCreateView,MemberUpdateView,MemberDeleteView

app_name = "members"




urlpatterns = [
    path("", MemberListView.as_view(), name="members-list"),
    path('<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('create/', MemberCreateView.as_view(), name='member_create'),
    path('<int:pk>/update/', MemberUpdateView.as_view(), name='member_update'),
    path('<int:pk>/delete/', MemberDeleteView.as_view(), name='member_delete'),

]
