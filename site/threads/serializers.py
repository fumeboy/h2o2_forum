from rest_framework import serializers

from boards.models import Board
from users.models import User

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    board = serializers.SlugRelatedField(slug_field='slug', queryset=Board.objects.all())
    # bookmark = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'content',
                  'created', 'board')
