from django.shortcuts import render
from rest_framework import generics
from .serializers import SkillSerializer
from .models import Skill

# Create your views here.
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = SkillSerializer # tell django what serializer to use

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all().order_by('id')
    serializer_class = SkillSerializer
    
    # New function-based view
