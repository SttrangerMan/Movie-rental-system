from rest_framework.views import APIView, status, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import get_object_or_404
from users.serializers import UserSerializer
from .permissions import isEmployer
from .models import User
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isEmployer]

    def get(self, request: Request, user_id):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
