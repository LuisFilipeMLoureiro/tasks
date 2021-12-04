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
@api_view(['GET', 'POST'])
def GET_POST(request):

    if request.method == 'GET':
        get = Task.objects.all()
        response = serializers.serialize("json", get)
        return HttpResponse(response, content_type="application/json", status=status.HTTP_200_OK)

    else:
        if request.method == 'POST':
            response_post = TaskSerializer(data=request.data)
            if response_post.is_valid():
                response_post.save()
                return JsonResponse(response_post.data, status=status.HTTP_201_CREATED)
            return JsonResponse(response_post.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DELETE(pk):

    response_get = Task.objects.get(pk=pk)
    response_get.delete()
    return JsonResponse({"deletado!"}, status=status.HTTP_200_OK)



    '''
    Referencias:
    [1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
    [2] - https://www.django-rest-framework.org/tutorial/quickstart/ 
        
    '''