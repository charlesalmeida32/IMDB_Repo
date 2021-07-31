import rest_framework
from rest_framework.permissions import BasePermission

class MyPermissions(BasePermission):
    '''The permissions set here will allow the a normal user to access only the GET API request and staff user to access 
    all of the request methods'''
    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_active:
            return True
        if request.method in ['GET', 'POST','PUT','DELETE', 'PATCH'] and request.user.is_staff:
            return True

        return False
