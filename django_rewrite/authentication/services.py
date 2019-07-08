from typing import Dict

from rest_framework import serializers
from users.models import Profile, User


class _UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class _ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.FileField()

    class Meta:
        model = Profile
        fields = [
            'description',
            'avatar'
        ]


def get_user_data(*, user: User) -> dict:
    user_data = _UserSerializer(instance=user).data
    return {**user_data}


def get_full_user_data(*, user: User) -> dict:
    profile_data = _ProfileSerializer(instance=user.profile).data
    return {**get_user_data(user=user), **profile_data}


def update_user_data(*, user: User, data: Dict[str, str]) -> dict:
    import ipdb; ipdb.set_trace()
