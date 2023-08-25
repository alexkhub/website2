from rest_framework import permissions


class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.slug == request.user.slug:
            return True
        return False
