from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


def get_null_user():
    return get_user_model().objects.get_or_create(username='deleted')


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    content = models.TextField(max_length=1024)
    author = models.ForeignKey(get_user_model(), related_name='comments',
                               on_delete=models.SET(get_null_user))
    thread = models.ForeignKey("threads.Post", related_name='comments', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
