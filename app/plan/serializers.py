from django.contrib.auth.models import User, Group
from rest_framework import serializers
from plan.models import Student, Plan, PlanCourse, PlanRequirement
from concentration.serializers import NestedConcentrationSerializer, NestedReqSerializer, CourseSerializer

class StudentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Student
    fields = ['name', 'plans']

class PlanSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Plan
    fields = ['submission_date', 'student', 'concentration', 'status', 'requirements']

class PlanCourseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PlanCourse
    fields = ['course']

class PlanRequirementSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PlanRequirement
    fields = ['requirement', 'course']

class NestedPlanCourseSerializer(serializers.Serializer):
  course = CourseSerializer()

class NestedPlanReqSerializer(serializers.Serializer):
  requirement = NestedReqSerializer()
  course = NestedPlanCourseSerializer(many=True)

class NestedPlanSerializer(serializers.Serializer):
  submission_date = serializers.DateField()
  status = serializers.CharField(max_length=255)
  concentration = NestedConcentrationSerializer()
  plan_requirements = NestedPlanReqSerializer(many=True)

class NestedStudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=255)
  plans = NestedPlanSerializer(many=True)

  