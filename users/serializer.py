from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phonenumber already exists')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
