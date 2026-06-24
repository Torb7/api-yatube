from django.urls import path, include
from rest_framework import routers

from . import views

v_1_router = routers.DefaultRouter()
v_1_router.register('posts', views.PostViewSet, basename='posts')


urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v_1_router.urls)),
]
