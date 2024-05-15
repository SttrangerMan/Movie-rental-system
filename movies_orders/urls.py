from django.urls import path
from .views import Movie_order_view

urlpatterns = [
    path("movies/<int:movie_id>/orders/", Movie_order_view.as_view()),
]
