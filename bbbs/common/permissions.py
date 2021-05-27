from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.profile.is_admin


class IsRegionModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_region_moderator

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.profile.is_region_moderator


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_moderator

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.profile.is_moderator


class IsMentor(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_mentor

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.profile.is_mentor

