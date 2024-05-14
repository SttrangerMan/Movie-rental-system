from rest_framework import serializers
from .models import Movie, RATING_CHOICES
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, allow_null=True, default=None, allow_blank=True
    )
    rating = serializers.ChoiceField(
        choices=RATING_CHOICES.choices, default=RATING_CHOICES.G
    )
    synopsis = serializers.CharField(default="", allow_null=True, allow_blank=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: User):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
