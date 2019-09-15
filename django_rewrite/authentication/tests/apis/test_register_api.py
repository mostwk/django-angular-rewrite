from django.urls import reverse

import pytest
from users.models import User

REGISTER_URL = reverse('api:auth:register')


@pytest.mark.parametrize(
    'data', [
        {'username': '', 'password': ''},
        {'username': 'user', 'password': ''},
        {'username': '', 'password': 'password'},
        {'username': 'user', 'password': 'pass'},
    ]
)
@pytest.mark.django_db
def test_register_api_with_bad_request(api_user, data):
    response = api_user.post(REGISTER_URL, data)

    assert response.status_code == 400


@pytest.mark.django_db
def test_register_api_with_good_request(api_user, register_request_data):
    assert User.objects.count() == 0

    response = api_user.post(REGISTER_URL, register_request_data)

    assert response.status_code == 201
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_register_api_with_duplicate_user(api_user, register_request_data):
    assert User.objects.count() == 0

    response = api_user.post(REGISTER_URL, register_request_data)

    assert response.status_code == 201
    assert User.objects.count() == 1

    response = api_user.post(REGISTER_URL, register_request_data)

    assert response.status_code == 400
    assert User.objects.count() == 1
