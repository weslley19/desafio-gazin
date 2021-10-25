
from .models import Users
from .serializers import UsersSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
