from django.shortcuts import render
from pizza_app.models import Pizza
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import ModelSerializer,PostSerialzer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
from django.db import IntegrityError
from json.decoder import JSONDecodeError
# Create your views here.
from django.http import HttpResponse
@api_view(['GET','POST','DELETE'])
def pizza_list(request):
    if request.method == 'GET':
        pizza= Pizza.objects.all() 
        pizza_type = request.query_params.get('pizza_type', None)
        pizza_size=request.query_params.get('pizza_size', None)
        toppings=request.GET.get('toppings',None)
        if pizza_type is not None :
            pizza =Pizza.objects.all().filter(pizza_type=pizza_type)
        if pizza_size is not None:
            pizza=Pizza.objects.all().filter(pizza_size=pizza_size)
        pizza_serializer = ModelSerializer(pizza, many=True)
        return JsonResponse(pizza_serializer.data, safe=False)

    if request.method == 'POST':
        pizza_size = request.data.get('pizza_size',None)
        pizza_type = request.data.get('pizza_type',None)
        toppings = request.data.get('toppings',None)
        pizza_serializer=PostSerialzer(data=request.data)
        data={}
        if pizza_serializer.is_valid():
            try:
                pizza=pizza_serializer.save()
                data['response']="successfully Added new entry"
                data['pizza_size']=pizza.pizza_size
                data['pizza_type']=pizza.pizza_type
                data['toppings']=pizza.toppings
                return Response(data)
            except AttributeError: 
                return HttpResponse("No such Key!!!!")
        else:
            data=serializer.errors
            return Response(data)
    if request.method == 'DELETE':
        count = Pizza.objects.all().delete()
        return JsonResponse({'message': '{} Pizza were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("YOUR REQUEST IS INVALID")

@api_view(['PUT', 'DELETE'])
def pizza_detail(request, pk):
    try: 
        pizza = Pizza.objects.get(pk=pk) 
    except Pizza.DoesNotExist: 
        return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'PUT': 
        pizza_data = JSONParser().parse(request) 
        pizza_serializer = ModelSerializer(pizza, data=pizza_data) 
        if pizza_serializer.is_valid(): 
            pizza_serializer.save() 
            return JsonResponse(pizza_serializer.data) 
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        pizza.delete() 
        return JsonResponse({'message': 'Pizza was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        