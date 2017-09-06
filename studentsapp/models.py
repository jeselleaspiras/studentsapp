from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    college = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.TextField()
    units = models.CharField(max_length=2)

    def __str__(self):
        return self.college

class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=50)
    address = models.TextField(max_length=200)
    course = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

