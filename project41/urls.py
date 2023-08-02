"""
URL configuration for project41 project.

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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_render/',data_render.as_view(),name='data_render'),
    path('fbv_insert/',fbv_insert,name='fbv_insert'),
    path('cbv_insert/',cbv_insert.as_view(),name='cbv_insert'),
    path('Temp/',Temp.as_view(),name='Temp'),

    path('haritha/',TemplateView.as_view(template_name='haritha.html'),name='haritha'),
]
