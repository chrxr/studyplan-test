from django.db import models

# Create your models here.

class Course(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Condition(models.Model):
  trigger = models.ForeignKey(Course, on_delete=models.CASCADE)
  is_present = models.BooleanField()
  hide = models.BooleanField()

class Requirement(models.Model):
  name = models.CharField(max_length=255)
  course = models.ManyToManyField(Course)
  min_courses = models.IntegerField(blank=True, null=True)
  max_courses = models.IntegerField(blank=True, null=True)
  allows_other = models.BooleanField(default=False)
  condition = models.ManyToManyField(Condition)

  def __str__(self):
    return self.name

class Concentration(models.Model):
  name = models.CharField(max_length=255)
  requirement = models.ManyToManyField(Requirement, related_name='concentrations')

  def __str__(self):
    return self.name


