from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.SkillList.as_view(), name='skill_list'), # api/contacts will be routed to the ContactList view for handling
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skill_detail'), # api/contacts will be routed to the ContactDetail view for handling
]