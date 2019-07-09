from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from users.models import User

from .permissions import JSONWebTokenAuthenticationMixin
from users.services import (
    get_user_data,
    get_full_user_data,
    update_user_data,
    update_user_profile,
)


class RegistrationApi(APIView):
    authentication_classes = ()
    permission_classes = ()

    class Serializer(serializers.ModelSerializer):
        password = serializers.CharField(
            max_length=128,
            min_length=8,
            write_only=True,
        )
        token = serializers.CharField(read_only=True)

        class Meta:
            model = User
            fields = ['username', 'password', 'token']

    def post(self, request):
        serializer = self.Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginApi(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = data.get('user')
        token = data.get('token')

        full_data = get_user_data(user=user)
        full_data.update({'token': token})

        return Response(full_data)


class UserDetailApi(JSONWebTokenAuthenticationMixin, APIView):
    def get(self, request):
        user_data = get_user_data(user=request.user)

        return Response(user_data)

    def patch(self, request):
        new_user_data = update_user_data(user=request.user, data=request.data)

        return Response(new_user_data)


class UserProfileApi(JSONWebTokenAuthenticationMixin, APIView):
    def get(self, request):
        full_user_data = get_full_user_data(user=request.user)

        return Response(full_user_data)

    def patch(self, request):
        new_user_profile = update_user_profile(
            user=request.user, data=request.data)

        return Response(new_user_profile)
