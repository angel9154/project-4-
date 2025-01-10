from django.urls import path
from . import views

urlpatterns = [
    path('api/skills', views.SkillList.as_view(), name='skill_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/skills/<int:pk>', views.SkillDetail.as_view(), name='skill_detail'), # api/contacts will be routed to the ContactDetail view for handling
]