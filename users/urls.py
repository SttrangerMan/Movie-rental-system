# musicians/urls.py
from django.urls import path
from .views import MusicianView

urlpatterns = [path("users/", MusicianView.as_view())]
