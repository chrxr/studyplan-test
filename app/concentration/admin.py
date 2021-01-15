from django.contrib import admin
from .models import Concentration, Requirement, Course, Condition

# Register your models here.

class ConcentrationAdmin(admin.ModelAdmin):
  model = Concentration
  filter_horizontal = ('requirement',)

class ConditionAdmin(admin.ModelAdmin):
  pass

class RequirementAdmin(admin.ModelAdmin):
  model = Requirement
  filter_horizontal = ('course',)
  filter_horizontal = ('condition',)

class CourseAdmin(admin.ModelAdmin):
  pass

admin.site.register(Concentration, ConcentrationAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Condition, ConditionAdmin)