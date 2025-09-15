from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        action = getattr(view, "action", None)
        if action in ["list", "retrieve"]:
            return IsAuthenticated().has_permission(request, view)
        elif action is None and request.method == "GET":
            return IsAuthenticated().has_permission(request, view)
        return IsAdminUser().has_permission(request, view)
