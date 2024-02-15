from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from newsletter.models import Suscriptor, Template

class SuscriptorSerializer(ModelSerializer):
  class Meta:
    model = Suscriptor
    fields = ['email', 'name','suscribed']
    read_only_fields = ['email']

class CreateSuscriptorSerializer(ModelSerializer):
  class Meta:
    model = Suscriptor
    fields = ['email', 'name']

class UnsuscribeSerializer(serializers.Serializer):
  email = serializers.EmailField()
  suscribed = serializers.BooleanField()

  def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.suscribed = validated_data.get('suscribed', instance.suscribed)
    instance.save()
    return instance

class TemplateSerializer(ModelSerializer):
  class Meta:
    model = Template
    fields = ['name','subject', 'content','category_id']