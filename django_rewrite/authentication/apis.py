from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.exceptions import ValidationError
from users.models import User

from .services import get_user_data


class RegistrationApi(APIView):
    authentication_classes = ()
    permission_classes = ()

    class Serializer(serializers.ModelSerializer):
        username = serializers.CharField(max_length=20, min_length=5)
        password = serializers.CharField(
            max_length=128,
            min_length=8,
            write_only=True,
        )
        token = serializers.CharField(read_only=True)

        class Meta:
            model = User
            fields = ['username', 'password', 'token']

        def validate(self, data):
            username = data.get('username')
            if User.objects.filter(username=username).exists():
                raise ValidationError(
                    {'username': 'this username is already taken'})

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)

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
