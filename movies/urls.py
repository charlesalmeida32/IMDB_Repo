from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

#URL to access the API "(domain or ip or localhost)/movies/movies_root_api/movies_root_api/"
movies_admin_route = DefaultRouter()
movies_admin_route.register('movies_root_api',views.AdminMovieApiView, basename='movies_root_api')

urlpatterns = [
    url(r'^movies_root_api/', include(movies_admin_route.urls)),
]
