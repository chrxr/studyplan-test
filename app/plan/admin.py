from django.contrib import admin
from .models import Student, Plan, PlanRequirement, PlanCourse

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  pass

class PlanAdmin(admin.ModelAdmin):
  pass

class PlanRequirementAdmin(admin.ModelAdmin):
  model = PlanRequirement
  filter_horizontal = ('course',)

class PlanCourseAdmin(admin.ModelAdmin):
  pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanRequirement, PlanRequirementAdmin)
admin.site.register(PlanCourse, PlanCourseAdmin)