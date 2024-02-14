from rest_framework.serializers import ModelSerializer
from newsletter.models import Suscriptor

class SuscriptorSerializer(ModelSerializer):
  class Meta:
    model = Suscriptor
    fields = ['email', 'name','suscribed']

class CreateSuscriptorSerializer(ModelSerializer):
  class Meta:
    model = Suscriptor
    fields = ['email', 'name']