from django.db import models
from concentration.models import Concentration, Course, Requirement

# Create your models here.

STATUS_CHOICES = [
    ('APPROVED', 'Approved'),
    ('DENIED', 'Denied'),
    ('INPROGRESS', 'In progress'),
]

class Student(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Plan(models.Model):
  submission_date = models.DateField(auto_now=True)
  student = models.ForeignKey(Student, related_name='plans', on_delete=models.CASCADE)
  concentration = models.ForeignKey(Concentration, default=0, on_delete=models.CASCADE)
  status = models.CharField(choices=STATUS_CHOICES, default='INPROGRESS', max_length=255)

class PlanCourse(models.Model):
  course = models.ForeignKey(Course, default=0, on_delete=models.CASCADE)

class PlanRequirement(models.Model):
  requirement = models.ForeignKey(Requirement, default=0, on_delete=models.CASCADE)
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_requirements')
  course = models.ManyToManyField(PlanCourse)



  # https://stackoverflow.com/questions/54791386/django-converting-queryset-with-foreign-keys-to-json