from django.db import models
from django.conf import settings

# Create your models here.
class Problem(models.Model):
    solved_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='solved_problems')
    name = models.CharField(max_length=30)
    problem_num = models.IntegerField()
    rank = models.CharField(max_length=5)


class ProblemClass(models.Model):
    problems = models.ManyToManyField(Problem, related_name='classes')
    name = models.CharField(max_length=30)
    ProblemClass_num = models.IntegerField(blank=True)

