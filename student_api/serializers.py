from rest_framework import serializers 
from .models import Student  # Import Skill model
from skill_api.models import Skill
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'skill')  # Only include the id and skill field

class StudentSerializer(serializers.ModelSerializer):
    # For writing, use PrimaryKeyRelatedField (which expects the skill ID)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all())

    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'skill')

    # Overriding the `to_representation` method to use the SkillSerializer for reading
    def to_representation(self, instance):
        # Get the original representation (i.e., the data as it is serialized)
        representation = super().to_representation(instance)

        # Manually serialize the `skill` field using the SkillSerializer for GET requests
        # Replace the skill ID with the serialized `skill` object
        skill_instance = instance.skill
        if skill_instance:
            representation['skill'] = SkillSerializer(skill_instance).data

        return representation




# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'name', 'age', 'skillId',)