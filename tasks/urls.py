from django.conf.urls import url 
from tasks import views 
from django.urls import path
 
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>', views.delete_task, name="delte"),
    path('all_tasks/', views.get_all_tasks, name="all_task"),
    path('post/', views.post_tasks, name="post"),
]