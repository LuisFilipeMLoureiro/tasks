from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.



@api_view(['GET', 'POST', 'DELETE'])
def tasks(request):

    
    if request.method == 'GET':
        ALL_TASKS = Task.objects.all()
        tasks_serializer = TaskSerializer(ALL_TASKS, many=True)
        title = request.GET.get('title', None)
        if title is not None:
            tasks = ALL_TASKS.filter(title__icontains=title)
        
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
        

    elif request.method == 'POST':
        POST_RECEBIDO = JSONParser().parse(request)
        TASK_POST= TaskSerializer(data=POST_RECEBIDO)
        if TASK_POST.is_valid():
            TASK_POST.save()
            return JsonResponse(TASK_POST.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(TASK_POST.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        DELETADO_N = Task.objects.all().delete()
        return JsonResponse({'message': '{} unidades deletadas'.format(DELETADO_N   [0])}, status=status.HTTP_204_NO_CONTENT)



'''
Referencias:

[1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
[2] - https://www.django-rest-framework.org/tutorial/quickstart/

'''