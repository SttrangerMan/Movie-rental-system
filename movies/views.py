from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, status, Request, Response
from .pagination import CustomPageNumberPagination
from rest_framework.generics import get_object_or_404
from .permissions import MyCustomPermission
from .serializers import MovieSerializer
from .models import Movie


class MoviesViews(APIView, CustomPageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class MoviesDetailsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
