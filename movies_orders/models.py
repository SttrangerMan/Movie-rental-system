from django.db import models


class MovieOrder(models.Model):

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_order"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_Movies_order"
    )

    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
