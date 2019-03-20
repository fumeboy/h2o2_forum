from rest_framework import serializers

from threads.models import Post
from users.models import User

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    thread = serializers.SlugRelatedField(slug_field='id', queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content',
                  'created', 'thread')
