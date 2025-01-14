from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import StudentSerializer
from django.http import JsonResponse
from student_api.models import Student
from company_api.models import Company

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = StudentSerializer # tell django what serializer to use

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

def get_compatible_entities(request):
    # Fetch all students and companies, linking via skill_id
    compatible = []
    students = Student.objects.select_related('skill').all()
    companies = Company.objects.select_related('skill').all()

    for student in students:

         # Find companies that share the same skill
        student_companies = []

        for company in companies:
            if student.skill == company.skill:  # Match skill_id
                student_companies.append(company.name)

        if student_companies:
            compatible.append({
                "student_name": student.name,
                "student_skill": student.skill.skill,
                "companies": student_companies  # List of companies for this student
            })

    return JsonResponse(compatible, safe=False)