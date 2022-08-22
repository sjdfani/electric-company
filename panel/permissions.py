from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_superuser)


class IsAdminOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        return (request.user and (request.user.is_staff or request.user.is_superuser))
