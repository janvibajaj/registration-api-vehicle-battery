from django.http import HttpResponse
from django.shortcuts import render
from .models import RegistrationList
from .serializers import RegistrationListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegistrationListAPIView(APIView):
    def get(self,request):
        details = RegistrationList.objects.all()
        serializer = RegistrationListSerializer(details,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RegistrationListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class RegistrationDetails(APIView):
    
    def get_object(self,id):
        try:
            return RegistrationList.objects.get(id=id)
        except RegistrationList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        registrationDetail = self.get_object(id)
        serializer = RegistrationListSerializer(registrationDetail)
        return Response(serializer.data)
    
    def put(self,request,id):
        registrationDetail = self.get_object(id)
        serializer = RegistrationListSerializer(registrationDetail,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        registrationDetail = self.get_object(id)
        registrationDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

    
        
