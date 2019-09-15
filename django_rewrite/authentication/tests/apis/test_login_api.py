from django.urls import reverse

import pytest
from users.models import User

LOGIN_URL = reverse('api:auth:login')


@pytest.mark.django_db
def test_login_api_with_good_request(api_user, registered_user_data):
    assert User.objects.count() == 1

    response = api_user.post(LOGIN_URL, registered_user_data)
    assert response.json()['token']

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_api_with_bad_request(api_user, registered_user_data):
    assert User.objects.count() == 1

    new_registered_user_data = {
        'username': 'custom_username',
        'password': 'custom_password'
    }
    assert new_registered_user_data != registered_user_data

    response = api_user.post(LOGIN_URL, new_registered_user_data)

    assert response.status_code == 400
    assert User.objects.count() == 1
