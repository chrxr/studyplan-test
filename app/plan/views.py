from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from plan.serializers import PlanSerializer, StudentSerializer, PlanRequirementSerializer, PlanCourseSerializer, NestedStudentSerializer
from plan.models import Plan, Student, PlanRequirement, PlanCourse


class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlanRequirementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlanRequirement.objects.all()
    serializer_class = PlanRequirementSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlanCourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlanCourse.objects.all()
    serializer_class = PlanCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class NestedStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = NestedStudentSerializer
    permission_classes = [permissions.IsAuthenticated]