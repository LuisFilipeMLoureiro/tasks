from django.shortcuts import render
from django.http.response import JsonResponse,Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.core import serializers

#verbos https

@api_view(['GET'])
def get_all_tasks(request):
    all_tasks = Task.objects.all()
    json_response = serializers.serialize("json", all_tasks)
    return HttpResponse(json_response, content_type="application/json", status=status.HTTP_200_OK)

@api_view(['POST'])
def post_tasks(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # json_response = serializers.serialize("json", serializer)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
    except Task.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "Task deletada com sucesso"}, status=status.HTTP_200_OK)



    '''
    Referencias:
    [1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
    [2] - https://www.django-rest-framework.org/tutorial/quickstart/ 
        
    '''