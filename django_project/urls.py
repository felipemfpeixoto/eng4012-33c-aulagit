"""django_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from appdoxopeito import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('title/', views.list_titles, name = "titles-list"),
    path('person/', views.list_people, name='people-list'),
    path('title/create/', views.create_title),
    path('person/create/', views.create_person),
    path('edit_title/<item_id>/', views.edit_title),
    path('remove_title/<item_id>/', views.remove_title),
    path('edit_person/<item_id>/', views.edit_person),
    path('remove_person/<item_id>/', views.remove_person),
]
