from damage.models import DamageReport, AdditionalDocument, Operator, Suggestion, TypeOfDamage
from rest_framework import serializers
from users.models import User


class PanelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('api_key',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class PanelDamageReportSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    additional_documents = serializers.SerializerMethodField()

    class Meta:
        model = DamageReport
        fields = '__all__'
    
    def update(self, instance, validated_data):
        request = self.context['request']
        damage_report = super().update(instance, validated_data)
        damage_docs_names = ['last_bill_image', 'national_card_image', 'ownership_doc_image']
        for name, file in request.FILES.items():
            if name not in damage_docs_names:
                AdditionalDocument.objects.create(damage_report=damage_report, image=file)
        return damage_report

    def get_created_at(self, obj):
        return obj.created_at.timestamp()

    def get_additional_documents(self, obj):
        request = self.context['request']
        result = []
        for doc in obj.additional_documents.all():
            result.append({
                'id': doc.pk,
                'url': request.build_absolute_uri(doc.image.url)
            })
        return result


class PanelAdditionalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalDocument
        fields = '__all__'


class PanelTypeOfDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDamage
        fields = '__all__'


class PanelOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class PanelSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'
