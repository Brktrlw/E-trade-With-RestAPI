from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):

        return obj.user == request.user
