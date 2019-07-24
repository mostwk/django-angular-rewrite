from django.conf.urls import include, url
from rest_framework import routers

from django_rewrite.posts import apis

app_name = 'posts'

router = routers.DefaultRouter()
router.register(r'posts', apis.PostsApi)
# router.register(r'posts/(?P<post_id>.+?)/comments', views.apis.CommentApi)

urlpatterns = [
    url(r'^', include(router.urls)),
]
