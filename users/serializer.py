from rest_framework import serializers
from .models import User
import uuid
from prop_project.settings import Redis_object
from .utils import number_generator


class RegisterUserSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class RegisterOperatorSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_staff = True
        user.api_key = uuid.uuid4().hex
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=20)

    def validate_phone_number(self, value):
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')
        return value


class ForgotPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)

    def validate_phone_number(self, value):
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')
        return value

    def process(self, validated_data):
        phone_number = validated_data['phone_number']
        code = number_generator(6)
        Redis_object.set(phone_number, code, ex=360)
        # send code to phone_number
        print(f"forgot password code: {code}")

    def save(self, **kwargs):
        self.process(self.validated_data)


class VerifyForgotPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    code = serializers.CharField(max_length=6)

    def validate_phone_number(self, value):
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')

    def process(self, validated_data):
        phone_number = validated_data['phone_number']
        code = validated_data['code']
        redis_code = Redis_object.get(phone_number)
        if redis_code:
            if redis_code == code:
                return (True, {'message': 'code is correct'})
            else:
                return (False, {'message': 'code is incorrect'})
        return (False, {'message': 'code is expired'})

    def save(self, **kwargs):
        return self.process(self.validated_data)


class ConfirmForgotPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_phone_number(self, value):
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone_number is not exists')
        return value

    def process(self, validated_data):
        phone_number = validated_data['phone_number']
        password = validated_data['password']
        user = User.objects.get(phone_number=phone_number)
        user.set_password(password)
        user.save()

    def save(self, **kwargs):
        self.process(self.validated_data)
