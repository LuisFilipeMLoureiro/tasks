from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.decorators import api_view



@api_view(['GET', 'POST', 'DELETE'])
def ENDPOINTS(request):

    if request.method == 'GET':
        t = Task.objects.all()
        series = TaskSerializer(t, many=True)
        
        return JsonResponse(series.data, safe=False)

    elif request.method == 'POST':
        t_post= JSONParser().parse(request)
        series_post = TaskSerializer(data=t_post)

        if series_post.is_valid():
            series_post.save()            
            return JsonResponse(series_post.data, status=status.HTTP_201_CREATED) 
            
        return JsonResponse(series_post.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



    '''
    Referencias:
    [1] - https://www.bezkoder.com/django-postgresql-crud-rest-framework/
    [2] - https://www.django-rest-framework.org/tutorial/quickstart/ 
        
    '''