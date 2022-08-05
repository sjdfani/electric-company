from rest_framework import serializers
from .models import User
from phonenumber_field.modelfields import PhoneNumberField


class RegisterUserSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    phonenumber = PhoneNumberField()
    password = serializers.CharField(max_length=20, write_only=True)
    type = serializers.CharField(max_length=20)

    def validate_phonenumber(self, value):
        if User.objects.filter(phonenumber=value).exists():
            raise serializers.ValidationError(
                'User with this phonenumber already exists')
        return value

    def validate_type(self, value):
        if value not in ['user', 'operator']:
            raise serializers.ValidationError(
                'Type must be either user or operator')
        return value

    def create(self, validated_data):
        type = validated_data.pop('type')
        if type == 'user':
            user = User.objects.create_user(**validated_data)
        else:
            user = User.objects.create_superuser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
