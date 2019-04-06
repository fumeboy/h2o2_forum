from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class NotificationList(ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def post(self, request, *args, **kwargs):
        resp = {'success': 1}

        sendto_list = request.data['sendto'].split(',')
        print(sendto_list)
        for one in sendto_list:
            if one is not '':
                temp = request
                temp.data['sendto'] = one
                self.create(temp, *args, **kwargs)

        return Response(resp, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        print(request.data['sendto'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)

    def get_queryset(self):
        return Notification.objects.filter(sendto=self.request.user)
