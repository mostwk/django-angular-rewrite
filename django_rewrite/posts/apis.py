from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from common.mixins import RatedApiMixin
from posts.models import Post
from posts.permissions import IsAuthenticatedOrPostAuthor


class PostsApi(RatedApiMixin, ModelViewSet):

    class Serializer(serializers.ModelSerializer):
        author = serializers.CharField(required=False)
        created_at = serializers.DateTimeField(read_only=True)
        updated_at = serializers.DateTimeField(read_only=True)
        votes = serializers.SerializerMethodField()

        class Meta:
            model = Post
            fields = [
                'id',
                'author',
                'title',
                'body',
                'votes',
                'created_at',
                'updated_at',
            ]

        def get_votes(self, obj):
            return obj.votes

    queryset = Post.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrPostAuthor, )
    serializer_class = Serializer

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
