from rest_framework.serializers import ModelSerializer
from studentsapp.models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('college', 'course', 'subject', 'units', 'description')

