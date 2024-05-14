from django.db import models


class RATING_CHOICES(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default="", blank=True, null=True)
    rating = models.CharField(
        max_length=20, choices=RATING_CHOICES.choices, default=RATING_CHOICES.G
    )
    synopsis = models.TextField(default="", null=True, blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
