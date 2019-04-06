from django.conf.urls import url
from django.urls import path
from .views import UserDetail, UserList, UsrThreadList, BookmarkList

urlpatterns = [
    url(r'(?P<username>[\w]*)/threads/$', UsrThreadList.as_view()),
    url(r'(?P<username>[\w]*)/bookmark/$', BookmarkList.as_view()),
    url(r'^$', UserList.as_view()),
    url(r'(?P<username>[\w]*)/$', UserDetail.as_view()),
]
