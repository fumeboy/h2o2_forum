from boards.models import Board
from users.models import User
from threads.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
