from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from newsletter.models import Suscriptor, Template, Category

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','topic',)

class TemplateSerializer(serializers.ModelSerializer):
    category_topic = serializers.CharField(source='category_id.topic', read_only=True)
    
    class Meta:
        model = Template
        fields = ('id','name', 'subject', 'content', 'category_id', 'category_topic', 'attached_file')

class RecipientSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SendEmailSerializer(serializers.Serializer):
  template_id = serializers.IntegerField()
  recipients = RecipientSerializer(many=True, allow_empty=True)
  class Meta:
    fields = ['template_id', 'recipients']
    read_only_fields = ['template_id', 'recipients']