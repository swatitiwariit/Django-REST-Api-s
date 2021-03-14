from django.db import models
from django.utils import timezone

# Create your models here.
class Designation(models.Model):
    title = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

