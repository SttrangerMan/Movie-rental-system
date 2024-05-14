from django.urls import path
from .views import MoviesDetailsViews, MoviesViews

urlpatterns = [
    path("movies/", MoviesViews.as_view()),
    path("movies/<int:movie_id>/", MoviesDetailsViews.as_view()),
]
