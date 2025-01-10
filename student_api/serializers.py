from rest_framework import serializers 
from .models import Student  # Import Skill model
from skill_api.models import Skill
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'skill')  # Only include the id and skill field

# Updated Student Serializer - include the Skill Serializer
class StudentSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()  # Add the SkillSerializer to serialize the related skill data

    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'skill')  # Use the 'skill' field (instead of 'skillId')




# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'name', 'age', 'skillId',)