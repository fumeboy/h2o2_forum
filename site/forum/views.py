from boards.models import Board
from users.models import User
from threads.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from boards.serializers import BoardSerializer
from threads.serializers import PostSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class HotBoard(ListAPIView):
    queryset = Board.objects.annotate(total_num=Count('posts')).order_by("-total_num")[:5]
    serializer_class = BoardSerializer
    permission_classes = (AllowAny,)


class HotThread(ListAPIView):
    queryset = Post.objects.annotate(total_num=Count('comments')).order_by("-total_num")[:5]
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


@api_view()
def forum_stats(request):
    """
    View returns details about the forum for
    the front page.
    """
    boards = Board.objects.all().count()
    users = User.objects.all().count()
    threads = Post.objects.all().count()
    return Response({"boards": boards, "users": users, "threads": threads})
