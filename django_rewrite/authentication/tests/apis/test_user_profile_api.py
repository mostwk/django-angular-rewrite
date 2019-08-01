import pytest
from django.urls import reverse
from users.models import User

USER_PROFILE_URL = reverse('api:auth:user-profile')


@pytest.mark.django_db
def test_get_user_profile_api_from_unauthenticated_user(
    api_user, registered_user_data
):
    assert User.objects.count() == 1

    response = api_user.get(USER_PROFILE_URL)

    assert response.status_code == 401


@pytest.mark.django_db
def test_get_user_profile_api_from_authenticated_user(
    authenticated_api_user, registered_user_data
):
    assert User.objects.count() == 1

    response = authenticated_api_user.get(USER_PROFILE_URL)

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_profile_api_update_user_data(
    authenticated_api_user, registered_user_data
):
    assert User.objects.count() == 1

    user = User.objects.get(username=registered_user_data.get('username'))

    new_user_data = {
        'description': 'My new description'
    }

    assert user.profile.description != new_user_data.get('description')

    response = authenticated_api_user.patch(USER_PROFILE_URL, new_user_data)

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.profile.description == new_user_data.get('description')
