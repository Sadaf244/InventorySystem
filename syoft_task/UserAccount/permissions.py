from rest_framework.permissions import BasePermission
from .models import *
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role=="Admin")

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role=="Manager")