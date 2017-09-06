from rest_framework import serializers
from .models import Post, Student

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('college', 'course', 'subject', 'description', 'units')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('student', 'name', 'address', 'course', 'date_created')
