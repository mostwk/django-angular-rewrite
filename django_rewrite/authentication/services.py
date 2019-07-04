from rest_framework import serializers

from users.models import User


class _UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]



def get_user_data(*, user: User) -> dict:
    user_data = _UserSerializer(instance=user).data
    return {**user_data}
