from django.db import models
# Create your models here.


class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.TextField()
    link = models.TextField(blank=True)
    have = models.BooleanField(default=False)
    sendto = models.ForeignKey("users.User", related_name='notify', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
