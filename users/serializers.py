from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.IntegerField(write_only=True)
    birthdate = serializers.DateField()
    is_employee = serializers.BooleanField()

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already taken.")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already registered.")

        return data
