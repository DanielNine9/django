from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsSeller(BasePermission):
    """
    Custom permission class to allow access only to staff and admin users.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is either a staff member or an admin
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
