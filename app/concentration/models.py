from django.db import models

# Create your models here.

class Concentration(models.Model):
  name = models.CharField(max_length=255)
  