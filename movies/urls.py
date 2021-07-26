from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

movies_route = DefaultRouter()
movies_route.register('movies_api',views.AdminMovieSerializer, basename='movies_api')

urlpatterns = [
    url(r'^movies_api/', include(movies_route.urls)),
]
