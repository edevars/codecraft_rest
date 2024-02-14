from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newsletter.models import Suscriptor
from newsletter.api.serializers import SuscriptorSerializer, CreateSuscriptorSerializer, UnsuscribeSerializer


class SuscriptorApiView(APIView):

  def get(self, request):
    suscriptors = Suscriptor.objects.all()
    serialized_suscriptors = SuscriptorSerializer(suscriptors, many=True)
    return Response(
      status=status.HTTP_200_OK,
      data=serialized_suscriptors.data
    )


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