from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField()

    class Meta:
        model = Notification
        fields = ('text', 'link', 'have', 'created')
