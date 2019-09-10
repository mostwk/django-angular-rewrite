from rest_framework import permissions


class IsAuthenticatedOrPostAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, post):
        if request.method in permissions.SAFE_METHODS:
            return True

        return post.author == request.user
