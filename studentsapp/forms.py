from django import forms
from .models import Post, Student

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('college', 'course', 'subject', 'description', 'units')

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student', 'name', 'address', 'course', 'date_created')