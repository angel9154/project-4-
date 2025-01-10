from django.urls import path
from . import views

urlpatterns = [
    path('api/students', views.StudentList.as_view(), name='student_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/students/<int:pk>', views.StudentDetail.as_view(), name='student_detail'), # api/contacts will be routed to the ContactDetail view for handling
]