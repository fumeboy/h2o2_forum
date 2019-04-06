from rest_framework import serializers

from .models import Notification
from users.models import User


class NotificationSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    sendto = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = ('text', 'link', 'have', 'created', 'sendto')
