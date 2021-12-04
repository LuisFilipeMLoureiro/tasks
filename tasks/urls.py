from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get, name="get"),
    path('post/', views.post, name="post"),
    path('tasks/<int:pk>', views.delete, name="delete"),   
    
]