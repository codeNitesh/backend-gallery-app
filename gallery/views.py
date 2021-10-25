from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer

from .models import Images
# Create your views here.


@api_view(['GET'])
def imageList(request):
	images = Images.objects.all().order_by('-imgId')
	serializer = ImageSerializer(images, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def imageDetail(request, pk):
	image = Images.objects.get(imgId=pk)
	serializer = ImageSerializer(image, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def imageCreate(request):
	serializer = ImageSerializer(data=request.data)
    
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
def imageUpdate(request, pk):
    image = Images.objects.get(imgId=pk)
    serializer = ImageSerializer(image, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def imageDelete(request, pk):
	image = Images.objects.get(imgId=pk)
	image.delete()

	return Response('Image succsesfully delete!')



