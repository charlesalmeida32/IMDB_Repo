from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Movies
from .serializer import MovieSerializer
from rest_framework.response import Response

# Create your views here.
class AdminMovieSerializer(ViewSet):
    '''This class will allow any admin user to do all of the CRUD operations on the database Movies using API'''
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def list(self, request):
        '''This method will help the admin user to retrive a all of record from the database'''
        obj = Movies.objects.all()
        serial = MovieSerializer(obj, many=True)
        return Response(serial.data)
        
    def retrieve(self, request, pk=None):
        '''This method will help the admin user to retrive a single record from the database'''
        obj = get_object_or_404(Movies, pk=pk)
        serial = MovieSerializer(obj)
        return Response(serial.data)

    def create(self, request):
        '''This method will help the admin user to create a new record in the database'''
        obj_data = request.data
        serial = MovieSerializer(data=obj_data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        '''This method will help the admin user to delete a single record from the database'''
        obj = get_object_or_404(Movies, pk=pk)
        obj.delete()
        return Response({"deleted":'true'}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        '''This method will help the admin user to fully update a record from the database'''
        data = request.data
        obj = get_object_or_404(Movies, pk=pk)
        serial = MovieSerializer(obj, data=data)
        if serial.is_valid():
            serial.save()
            return Response({'Data Updated':"True"}, status=status.HTTP_200_OK)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        '''This method will help the admin user to partially update a record from the database'''
        data = request.data
        obj = get_object_or_404(Movies, pk=pk)
        serial = MovieSerializer(obj, data=data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response({'Data Updated':"True"}, status=status.HTTP_200_OK)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# class AdminMovieSerializer(ModelViewSet):
#     '''This code will give access to get, post, put, patch, delete to the user having admin privilege'''
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAdminUser]

    