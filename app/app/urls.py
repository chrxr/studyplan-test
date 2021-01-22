"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from concentration import views
from plan import views as plan_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'concentrations', views.ConcentrationViewSet)
router.register(r'requirements', views.RequirementViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'conditions', views.ConditionViewSet)
router.register(r'plans', plan_views.PlanViewSet)
router.register(r'students', plan_views.StudentViewSet)
router.register(r'plan-requirement', plan_views.PlanRequirementViewSet)
router.register(r'plan-course', plan_views.PlanCourseViewSet)
router.register(r'nested-students', plan_views.NestedStudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
