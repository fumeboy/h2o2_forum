from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (SAFE_METHODS, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from utils.mixins import MultipleFieldLookupMixin
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def get_queryset(self):
        thread_id = self.kwargs['thread']
        return Comment.objects.filter(thread__id=thread_id)


class CommentDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_fields = ['id']
    lookup_url_kwargs = ['comment']
    model = Comment

    def check_object_permissions(self, request, obj):
        super(CommentDetail, self).check_object_permissions(request, obj)
        if request.method not in SAFE_METHODS and request.user != obj.author:
            self.permission_denied(request,
                                   message='User cannot edit this object.')

