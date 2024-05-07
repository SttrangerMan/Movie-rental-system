from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import User
from users.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        user = User.objects.create(**request.data)

        if user.is_valid():
            return Response(user, status.HTTP_201_CREATED)
        else:
            return serializer.erros
