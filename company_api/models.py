from django.db import models
from skill_api.models import Skill
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    skill = models.ForeignKey(Skill, related_name='companies', on_delete=models.CASCADE)  # Link to Skill model