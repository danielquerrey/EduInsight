"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('classes/', views.classes, name = "classes"),
    path('add-class/', views.add_teachers_class, name='add_teachers_class'),
    path('model-entries/', views.view_model_entries, name='view_model_entries'),
    path('selected-class/', views.single_class,name = 'single_class'),
    # path('new-entry/', views.create_entry, name='new-entry'),

] 
