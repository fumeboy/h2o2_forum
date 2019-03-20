from django.conf.urls import url
from django.urls import path
from .views import UserDetail, UserList, get_my_thread, get_usr_bookmark

urlpatterns = [
    url(r'(?P<username>[\w]*)/threads/$', get_my_thread),
    url(r'(?P<username>[\w]*)/bookmark/$', get_usr_bookmark),
    url(r'^$', UserList.as_view()),
    url(r'(?P<username>[\w]*)/$', UserDetail.as_view()),
]
