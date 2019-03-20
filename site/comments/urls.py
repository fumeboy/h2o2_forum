from django.conf.urls import url
from django.urls import path
from .views import CommentDetail, CommentList

urlpatterns = [
    url(r'^$', CommentList.as_view()),
    path('<int:comment>/', CommentDetail.as_view())
]
