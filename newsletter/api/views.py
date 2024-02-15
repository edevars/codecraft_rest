from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newsletter.models import Suscriptor, Template, Category
from newsletter.api.serializers import SuscriptorSerializer, CreateSuscriptorSerializer, UnsuscribeSerializer, TemplateSerializer
from newsletter.api.serializers import CategorySerializer
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
  
class TemplateApiView(APIView):
  def get(self, request):
    try:
      templates = Template.objects.all()
      serialized_templates = TemplateSerializer(templates, many=True)
      return Response(
        status=status.HTTP_200_OK,
        data=serialized_templates.data
      )
    except:
      return Response(serialized_templates.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def post(self, request):
    serializer = TemplateSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryApiView(APIView):
  def get(self, request):
    try:
      categories = Category.objects.all()
      serialized_category = CategorySerializer(categories, many=True)
      return Response(
        status=status.HTTP_200_OK,
        data=serialized_category.data
      )
    except:
      return Response(serialized_category.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def post(self, request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)