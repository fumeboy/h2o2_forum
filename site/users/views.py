from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Count
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (SAFE_METHODS, IsAuthenticatedOrReadOnly)
import json
from .models import User
from threads.models import Post
from threads.serializers import PostSerializer
from rest_framework.response import Response
from .serializers import PublicUserSerializer, PrivateUserSerializer
from rest_framework.pagination import PageNumberPagination


class UserList(ListCreateAPIView):
    # "A list of all registered users."
    serializer_class = PublicUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()


class UserDetail(RetrieveUpdateDestroyAPIView):
    # "A single user's account details."
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'username'
    model = User

    def update(self, request, *args, **kwargs):
        if request.data['flag']:
            print(request.data['bookmark'])
            obj = Post.objects.get(id=request.data['bookmark'])
            if request.data['flag'] == 1:
                request.user.bookmark.add(obj)
            else:
                request.user.bookmark.remove(obj)
            resp = {'message': "success"}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)

    def check_object_permissions(self, request, obj):
        super(UserDetail, self).check_object_permissions(request, obj)
        if request.method not in SAFE_METHODS and request.user.username != obj.username:
            self.permission_denied(request,
                                   message='User cannot edit this object.')

    def get_serializer_class(self):
        if self.request.user.username == self.kwargs['username']:
            return PrivateUserSerializer
        else:
            return PublicUserSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookmarkList(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def get_queryset(self):
        return self.request.user.bookmark.all()


class UsrThreadList(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
