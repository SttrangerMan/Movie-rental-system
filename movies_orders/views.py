from rest_framework.views import APIView, status, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import MyCustomPermission
from .serializer import Movie_order_serializer
from rest_framework.generics import get_object_or_404
from movies.models import Movie


class Movie_order_view(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request, movie_id):
        order = get_object_or_404(Movie, id=movie_id)

        serializer = Movie_order_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=order, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
