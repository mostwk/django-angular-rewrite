from rest_framework import permissions


class IsAuthenticatedOrPostAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user:
            return post.author == request.user
        return False
