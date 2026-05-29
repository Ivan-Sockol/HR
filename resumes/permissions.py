from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_hr_manager or request.user.is_admin:
                return True
            return obj.user == request.user
        return obj.user == request.user or request.user.is_admin

class CanCreateResume(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_candidate or request.user.is_admin
        return True

class CanDeleteResume(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_admin or request.user.is_candidate
        return True