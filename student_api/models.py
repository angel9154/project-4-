from django.db import models
from skill_api.models import Skill
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    # skillId = models.IntegerField()
    skill = models.ForeignKey(Skill, related_name='students', on_delete=models.CASCADE)  # Link to Skill model

    def __str__(self):
        return self.name