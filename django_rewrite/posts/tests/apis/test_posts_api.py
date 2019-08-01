import pytest
from django.urls import reverse
from posts.models import Post

POSTS_GET_URL = reverse('api:posts:post-list')


@pytest.mark.django_db
def test_posts_get_api(api_user, populate_posts):
    assert Post.objects.count() > 0

    response = api_user.get(POSTS_GET_URL)

    assert response.status_code == 200
