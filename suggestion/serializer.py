from rest_framework import serializers

from users.models import User
from .models import Suggestion


class UserSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number']


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['user'] = UserSuggestionSerializer(instance.user).data
        return res


class CreateSuggestionSerializer(serializers.Serializer):
    description = serializers.CharField()

    def create(self, validated_data):
        user = self.context['request'].user
        return Suggestion.objects.create(user=user, **validated_data)
