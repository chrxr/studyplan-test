from django.contrib.auth.models import User, Group
from rest_framework import serializers
from concentration.models import Concentration, Requirement, Course, Condition


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ConcentrationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Concentration
    fields = ['name', 'requirement']

class RequirementSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Requirement
    fields = ['name', 'min_courses', 'max_courses', 'allows_other', 'course', 'condition']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Course
    fields = ['name']

class ConditionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Condition
    fields = ['trigger', 'is_present', 'hide']

class NestedConditionSerializer(serializers.Serializer):
  trigger = CourseSerializer()
  is_present = serializers.BooleanField()
  hide = serializers.BooleanField()

class NestedReqSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=255)
  condition = NestedConditionSerializer(many=True)
  course = CourseSerializer(many=True)

class NestedConcentrationSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=255)
  requirement = NestedReqSerializer(many=True)