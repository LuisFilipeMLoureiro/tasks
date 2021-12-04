from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_tasks/', views.get, name="all_tasks"),
    path('post/', views.post, name="post"),
    path('tasks/<int:pk>', views.delete_task, name="delete"),   
    
]