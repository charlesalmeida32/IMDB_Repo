from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Movies
from .serializer import MovieSerializer
from rest_framework.response import Response
from .filter import MoviesFilter
from .custompermissions import MyPermissions


class AdminMovieApiView(ModelViewSet):
    '''This code will give access to get, post, put, patch, delete to the user having staff privilege.
    Any other active user will have access to get method only'''
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [MyPermissions]
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    filter_class = MoviesFilter


# class AdminMovieApiView(ViewSet):
#     '''This class will allow any admin user to do all of the CRUD operations on the database Movies using API
#     and other users will have access only to get method
#     This code will be used if your API requires heavy modification before sending Data the data'''
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [MyPermissions]
#     # filter_class = MoviesFilter
    

#     def list(self, request):
#         '''This method will help the admin user to retrive a all of record from the database'''
#         obj = Movies.objects.all()
#         serial = MovieSerializer(obj, many=True)
#         return Response(serial.data)
        
#     def retrieve(self, request, pk=None):
#         '''This method will help the admin user to retrive a single record from the database'''
#         obj = get_object_or_404(Movies, pk=pk)
#         serial = MovieSerializer(obj)
#         return Response(serial.data)

#     def create(self, request):
#         '''This method will help the admin user to create a new record in the database'''
#         obj_data = request.data
#         serial = MovieSerializer(data=obj_data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data, status=status.HTTP_201_CREATED)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         '''This method will help the admin user to delete a single record from the database'''
#         obj = get_object_or_404(Movies, pk=pk)
#         obj.delete()
#         return Response({"deleted":'true'}, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         '''This method will help the admin user to fully update a record from the database'''
#         data = request.data
#         obj = get_object_or_404(Movies, pk=pk)
#         serial = MovieSerializer(obj, data=data)
#         if serial.is_valid():
#             serial.save()
#             return Response({'Data Updated':"True"}, status=status.HTTP_200_OK)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         '''This method will help the admin user to partially update a record from the database'''
#         data = request.data
#         obj = get_object_or_404(Movies, pk=pk)
#         serial = MovieSerializer(obj, data=data, partial=True)
#         if serial.is_valid():
#             serial.save()
#             return Response({'Data Updated':"True"}, status=status.HTTP_200_OK)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)