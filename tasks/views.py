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

@api_view(['GET', 'POST', 'DELETE'])
def tasks(requisicao):

    if requisicao.method == 'GET':
        all_tasks = Task.objects.all()
        json_response = serializers.serialize("json", all_tasks)
        return HttpResponse(json_response, content_type="application/json", status=status.HTTP_200_OK)


    elif requisicao.method == 'POST':
        serializer = TaskSerializer(data=requisicao.data)
        if serializer.is_valid():
            serializer.save()        
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if requisicao.method == 'DELETE':
        tasks_deleted = Task.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(tasks_deleted[0])}, status=status.HTTP_204_NO_CONTENT)





    '''
    Referencias:
    [1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
    [2] - https://www.django-rest-framework.org/tutorial/quickstart/ 
        
    '''