from django.http import HttpResponse, JsonResponse, Http404
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework.parsers import JSONParser

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET'])
def get():
    response_get = Task.objects.all()
    json_get = serializers.serialize("json", response_get)
    return HttpResponse(json_get, content_type="application/json", status=status.HTTP_200_OK)

@api_view(['POST'])
def post(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete(pk):
    try:
        get = Task.objects.get(pk=pk)
        get.delete()
    except Task.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({"message": "Task deletada com sucesso"}, status=status.HTTP_200_OK)


    '''
    Referencias:
    [1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
    [2] - https://www.django-rest-framework.org/tutorial/quickstart/ 
        
    '''