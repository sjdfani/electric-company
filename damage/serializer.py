from rest_framework import serializers
from .models import DamageReport, AdditionalDocument, Operator, TypeOfDamage
from users.models import User
from phonenumber_field.serializerfields import PhoneNumberField


class CreateUserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'province',
                  'city', 'postal_code', 'national_code', 'address']


class CreateDamageReportSerializer(serializers.ModelSerializer):
    user = CreateUserSerializer()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = DamageReport
        exclude = ('operator',)
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        request = self.context['request']
        user_data = validated_data.pop('user')
        user = User.objects.filter(
            phone_number=user_data['phone_number']).first()
        if not user:
            user = User.objects.create(**user_data)
        damage_report = DamageReport.objects.create(
            user=user, **validated_data)
        damage_docs_names = ['last_bill_image',
                             'national_card_image', 'ownership_doc_image']
        for name, file in request.FILES.items():
            if name not in damage_docs_names:
                AdditionalDocument.objects.create(
                    damage_report=damage_report, image=file)
        return damage_report

    def get_created_at(self, obj):
        return obj.created_at.timestamp()


class TypeOfDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDamage
        fields = '__all__'


class ValidateDamageReportSerializer(serializers.Serializer):
    billing_id = serializers.CharField()
    unique_id = serializers.CharField()


class RetrieveOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class RetrieveDamageReportSerializer(serializers.ModelSerializer):
    operator = RetrieveOperatorSerializer()
    type_of_damage = TypeOfDamageSerializer()
    user = CreateUserSerializer()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = DamageReport
        fields = '__all__'

    def get_created_at(self, obj):
        return obj.created_at.timestamp()
