from django.conf.urls import url 
from tasks import views 
from django.urls import path
 
urlpatterns = [
    path("tasks/<int:pk>", views.DELETE, name="task"),
    path("tasks/", views.GET_POST, name="all_task"),


]