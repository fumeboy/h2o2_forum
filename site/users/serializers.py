from rest_framework.serializers import (DateTimeField, ModelSerializer,
                                        PrimaryKeyRelatedField, SerializerMethodField)

from threads.models import Post
from threads.serializers import PostSerializer
from rest_framework import serializers
from .models import User


class BaseUserSerializer(ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User


class PublicUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('username', 'avatar', 'date_joined', 'bio', 'bookmark')


class PrivateUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('username', 'avatar', 'email',
                  'date_joined', 'last_login', 'bio', 'bookmark')
