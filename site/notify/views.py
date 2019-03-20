from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class NotificationList(ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def get_queryset(self):
        return Notification.objects.filter(sendto=self.request.user.id)
