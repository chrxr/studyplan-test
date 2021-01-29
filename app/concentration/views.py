from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from concentration.serializers import UserSerializer, GroupSerializer, ConcentrationSerializer, RequirementSerializer, CourseSerializer, ConditionSerializer
from concentration.models import Concentration, Requirement, Course, Condition

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated|ReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

class ConcentrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Concentration.objects.all()
    serializer_class = ConcentrationSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

class RequirementViewSet(viewsets.ModelViewSet):
  queryset = Requirement.objects.all()
  serializer_class = RequirementSerializer
  permission_classes = [IsAuthenticated|ReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  permission_classes = [IsAuthenticated|ReadOnly]

class ConditionViewSet(viewsets.ModelViewSet):
  queryset = Condition.objects.all()
  serializer_class = ConditionSerializer
  permission_classes = [IsAuthenticated|ReadOnly]