from typing import Dict

from rest_framework import serializers
from users.models import Profile, User


class _GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class _UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
        ]


class _ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = [
            'description',
            'avatar'
        ]


def get_user_data(*, user: User) -> dict:
    user_data = _GetUserSerializer(instance=user).data
    return {**user_data}


def get_full_user_data(*, user: User) -> dict:
    profile_data = _ProfileSerializer(instance=user.profile).data
    return {**get_user_data(user=user), **profile_data}


def update_model_fields(obj, serializer, data):
    for field, value in data.items():
        if field in serializer.fields:
            setattr(obj, field, value)

    return obj


def update_user_data(*, user: User, data: Dict[str, str]) -> dict:
    serializer = _UpdateUserSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    user = update_model_fields(user, serializer, data)

    user.save()

    return {**get_user_data(user=user)}


def update_user_profile(*, user: User, data: Dict[str, str]) -> dict:
    serializer = _ProfileSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    user.profile = update_model_fields(user.profile, serializer, data)

    user.profile.save()

    return {**get_full_user_data(user=user)}
