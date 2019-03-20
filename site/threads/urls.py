from django.conf.urls import url, include
from django.urls import path
from .views import ThreadDetail, ThreadList
from comments.urls import urlpatterns as comment_patterns

urlpatterns = [
    url(r'^$', ThreadList.as_view()),
    path('<int:thread>/', ThreadDetail.as_view()),
    path('<int:thread>/comments/', include(comment_patterns))
]
