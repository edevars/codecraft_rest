from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from newsletter.models import Suscriptor, Template, Category, Newsletter
from newsletter.api.serializers import SuscriptorSerializer, CreateSuscriptorSerializer, UnsuscribeSerializer, TemplateSerializer, SendEmailSerializer, NewsletterSerializer
from newsletter.api.serializers import CategorySerializer
from .email_utils import send_email


class SuscriptorApiView(APIView):
  def get(self, request):
    try:
      suscriptors = Suscriptor.objects.all()
      serialized_suscriptors = SuscriptorSerializer(suscriptors, many=True)
      return Response(
        status=status.HTTP_200_OK,
        data=serialized_suscriptors.data
      )
    except:
      return Response(serialized_suscriptors.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def post(self, request):
    serializer = CreateSuscriptorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, *args, **kwargs):
    email = request.data['email']
    
    try:
      suscriptor = Suscriptor.objects.get(email=email)
    except Suscriptor.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UnsuscribeSerializer(suscriptor, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class TemplateDetailView(APIView):
  def get_object(self, pk):
    try:
      return Template.objects.get(pk=pk)
    except Template.DoesNotExist:
      raise Http404()

  def get(self, request, pk, format=None):
    instance = self.get_object(pk)
    serializer = TemplateSerializer(instance)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    instance = self.get_object(pk)
    serializer = TemplateSerializer(instance, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    instance = self.get_object(pk)
    instance.delete()

class TemplateListView(generics.ListCreateAPIView):
  queryset = Template.objects.all()
  serializer_class = TemplateSerializer
  parser_classes = (MultiPartParser, FormParser)

  def perform_create(self, serializer):
     attached_file = self.request.data.get('attached_file')
     serializer.save(attached_file=attached_file)

  def perform_update(self, serializer):
    attached_file = self.request.data.get('attached_file')
    serializer.save(attached_file=attached_file)

class CategoryListView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CategoryUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  lookup_field = 'pk'

  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)

class SendEmailView(APIView):
  def post(self, request):
    serializer = SendEmailSerializer(data=request.data)
    if serializer.is_valid():
      template_id = serializer.validated_data['template_id']
      recipients = serializer.validated_data['recipients']
      newsletter_name = serializer.validated_data['newsletter_name']
      try:
        success_emails = send_email(template_id, recipients, newsletter_name)
        return Response({'success': True, 'message': 'Emails sent successfully', 'success_emails_sent': len(success_emails)}, status=status.HTTP_200_OK)
      except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NewsletterListView(generics.ListCreateAPIView):
  queryset = Newsletter.objects.all()
  serializer_class = NewsletterSerializer