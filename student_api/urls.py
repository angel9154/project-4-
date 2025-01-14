from django.urls import path
from .views import StudentList, StudentDetail, get_compatible_entities
urlpatterns = [
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('compatibles/', get_compatible_entities, name='get_compatibles'),  # Use the imported function
]