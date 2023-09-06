from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Mobile
from .serializers import MobileSerializers
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class MobilesList(APIView):
    def get(self,request):
        lists = Mobile.objects.all()
        serializer = MobileSerializers(lists,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MobileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class MobileDetails(APIView):
    def get_object(self,id):
        try:
            return Mobile.objects.get(id = id)
        except Mobile.DoesNotExist:
            raise Http404
        

    def get(self,request,id):
        mobile = self.get_object(id)
        serializer = MobileSerializers(mobile)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,id):
        mobile = self.get_object(id)
        serializer = MobileSerializers(mobile,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK )
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def patch(self,request,id):
        moblie = self.get_object(id)
        serializer = MobileSerializers(moblie,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        moblie = self.get_object(id)
        moblie.delete()
        return Response({"msg":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)

