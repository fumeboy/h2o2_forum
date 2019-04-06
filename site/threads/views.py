from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (SAFE_METHODS, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from utils.mixins import MultipleFieldLookupMixin
from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ThreadList(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def post(self, request, *args, **kwargs):
        print(self)
        print(request.data)
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        board = self.kwargs['board']
        return Post.objects.filter(board__slug=board)


class ThreadDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_fields = ['id']
    lookup_url_kwargs = ['thread']
    model = Post

    def check_object_permissions(self, request, obj):
        super(ThreadDetail, self).check_object_permissions(request, obj)
        if request.method not in SAFE_METHODS and request.user != obj.author:
            self.permission_denied(request,
                                   message='User cannot edit this object.')


