from damage.models import DamageReport, AdditionalDocument, TypeOfDamage, Status
from rest_framework import serializers
from users.models import User
from django.utils import timezone


class PanelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('api_key', 'password')


class PanelDamageReportSerializer(serializers.ModelSerializer):
    additional_documents = serializers.SerializerMethodField()

    class Meta:
        model = DamageReport
        fields = '__all__'

    def update(self, instance, validated_data):
        request = self.context['request']
        damage_report = super().update(instance, validated_data)
        if damage_report.done_date == None and damage_report.status != Status.TODO:
            damage_report.done_date = timezone.now()
            damage_report.save()
        damage_docs_names = ['last_bill_image',
                             'national_card_image', 'ownership_doc_image']
        for name, file in request.FILES.items():
            if name not in damage_docs_names:
                AdditionalDocument.objects.create(
                    damage_report=damage_report, image=file)
        return damage_report

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['user'] = PanelUserSerializer(
            instance.user, context={'request': request}).data
        return res

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
        model = User
        exclude = ('api_key', 'password')
