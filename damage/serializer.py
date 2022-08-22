from rest_framework import serializers
from .models import DamageReport, AdditionalDocument, TypeOfDamage
from users.models import User


class CreateDamageReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamageReport
        exclude = ('operator',)
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        request = self.context['request']
        user_data = validated_data.pop('user')
        user = User.objects.filter(
            phone_number=user_data['phone_number']).first()
        damage_report = DamageReport.objects.create(
            user=user, **validated_data)
        damage_docs_names = ['last_bill_image',
                             'national_card_image', 'ownership_doc_image']
        for name, file in request.FILES.items():
            if name not in damage_docs_names:
                AdditionalDocument.objects.create(
                    damage_report=damage_report, image=file)
        return damage_report


class TypeOfDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDamage
        fields = '__all__'


class ValidateDamageReportSerializer(serializers.Serializer):
    billing_id = serializers.CharField()
    unique_id = serializers.CharField()


class RetrieveDamageReportSerializer(serializers.ModelSerializer):
    type_of_damage = TypeOfDamageSerializer()

    class Meta:
        model = DamageReport
        fields = '__all__'
