import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

import pytest
from posts.models import Post
from posts.tests.factories import PostFactory
from users.tests.factories import UserFactory

User = get_user_model()

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
def test_post_update_api():

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


@pytest.mark.parametrize(
    ('vote', 'result'), [
        (1, 1),
        (0, 0),
        (-1, -1),
    ]
)
@pytest.mark.django_db
def test_posts_single_user_rating_api(authenticated_api_user, vote, result):

    post = PostFactory()

    assert post.votes == 0

    post_rating_url = f'{POSTS_URL}{post.id}/vote/{vote}/'

    response = authenticated_api_user.post(post_rating_url)

    assert response.data.get('votes') == result

    assert post.votes == result


@pytest.mark.django_db
def test_posts_multiple_user_rating_api():

    number_of_users = random.randint(2, 10)

    api_client = APIClient()

    users = UserFactory.generate_batch('create', number_of_users)

    post = PostFactory()

    assert post.votes == 0

    post_rating_url = f'{POSTS_URL}{post.id}/vote/1/'

    for user in users:
        api_client.force_authenticate(user=user)
        api_client.post(post_rating_url)

    assert post.votes == number_of_users
