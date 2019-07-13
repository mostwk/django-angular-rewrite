import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User

REGISTER_URL = reverse('api:auth:register')
LOGIN_URL = reverse('api:auth:login')
USER_DETAIL_URL = reverse('api:auth:user-detail')
USER_PROFILE_URL = reverse('api:auth:user-profile')


@pytest.fixture
def api_user():
    return APIClient()


@pytest.fixture
def register_request_data():
    return {
        'username': 'test_user_1',
        'password': 'user1pass'
    }


@pytest.fixture
def registered_user_data(register_request_data):
    assert User.objects.count() == 0
    response = APIClient().post(REGISTER_URL, register_request_data)
    assert response.status_code == 201
    return register_request_data


@pytest.fixture
def authenticated_api_user(api_user, registered_user_data):
    user = User.objects.get(username=registered_user_data['username'])
    api_user.force_authenticate(user=user)
    return api_user
