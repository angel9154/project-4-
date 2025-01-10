from rest_framework import serializers 
from .models import Company 
from skill_api.models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'skill')

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
        model = Company # tell django which model to use
        fields = ('id', 'name', 'skill',) # tell django which fields to include