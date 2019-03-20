from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.aggregates import Count

from boards.models import Board


def get_null_user():
    return get_user_model().objects.get_or_create(username='deleted')


def get_null_board():
    return Board.objects.get_or_create(name='deleted')


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='posts',
                               on_delete=models.SET(get_null_user))
    board = models.ForeignKey(Board, related_name='posts',
                              on_delete=models.SET(get_null_board))

    def bookmark_num(self):
        return self.objects.annotate(num_posts=Count('bookmark'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']



