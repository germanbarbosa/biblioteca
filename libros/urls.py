"""libros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from biblioApp import views
from biblioApp.views.autorCreateView import AutorCreateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    
    path('api/autor/lista', views.AutorListApiView.as_view()),
    path('api/autor/create', views.AutorCreateView.as_view()),
    path('api/autor/detail/<pk>', views.AutorDetailView.as_view()),
    path('api/autor/delete/<pk>', views.AutorDeleteView.as_view(),),
    path('api/autor/update/<pk>', views.AutorUpdateView.as_view()),
    path('api/autor/modificar/<pk>', views.AutorRetriveUpdateView.as_view(),),
    
    path('api/libro/lista', views.LibroListApiView.as_view()),
    path('api/libro/create', views.LibroCreateView.as_view()),
    path('api/libro/detail/<pk>', views.LibroDetailView.as_view()),
    path('api/libro/delete/<pk>', views.LibroDeleteView.as_view(),),
    path('api/libro/update/<pk>', views.LibroUpdateView.as_view()),
    path('api/libro/modificar/<pk>', views.LibroRetriveUpdateView.as_view(),),
]