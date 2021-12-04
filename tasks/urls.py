from django.conf.urls import url 
from tasks import views 
from django.urls import path
 
urlpatterns = [ 
    path('tasks/<int:pk>', views.DELETE, name="delte"),
    path('all_tasks/', views.GET, name="all_task"),
    path('post/', views.POST, name="post"),
]