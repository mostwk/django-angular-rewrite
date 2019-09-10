import pytest
from django.urls import reverse
from posts.models import Post
from posts.tests.factories import PostFactory
from rest_framework.test import APIClient
from users.tests.factories import UserFactory

POSTS_URL = reverse('api:posts:post-list')


@pytest.mark.django_db
def test_posts_get_api(api_user, populate_posts):
    assert Post.objects.count() > 0

    response = api_user.get(POSTS_URL)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_create_api(api_user, authenticated_api_user):

    data = {
        'title': 'My post title',
        'body': 'My post body',
    }

    response = api_user.post(POSTS_URL, data=data)

    assert response.status_code == 401

    response = authenticated_api_user.post(POSTS_URL, data=data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_post_update_api(api_user):

    user_1 = UserFactory()
    user_2 = UserFactory()

    post = PostFactory(author=user_2)
    post_detail_url = f'{POSTS_URL}{post.id}/'

    request_data = {
        'title': 'Changed post title',
        'body': 'My post body',
    }

    assert post.title != request_data.get('title')
    assert post.body != request_data.get('body')

    api_user_1 = APIClient()
    api_user_1.force_authenticate(user=user_1)
    response = api_user_1.put(post_detail_url, data=request_data)

    assert response.status_code == 403

    api_user_2 = APIClient()
    api_user_2.force_authenticate(user=user_2)
    response = api_user_2.put(post_detail_url, data=request_data)

    assert response.status_code == 200
    assert response.data.get('title') == request_data.get('title')
    assert response.data.get('body') == request_data.get('body')
