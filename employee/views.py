from django.shortcuts import render
from django.http import HttpResponse
from .models import employees
from .serializers import emp_serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def emp(request):
    if request.method == 'GET':    
        queryset = employees.objects.all()
        serializer = emp_serializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = emp_serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def emp_details(request, pk):
    try:
        emp = employees.objects.get(pk=pk)
    except employee.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = emp_serializers(emp)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = emp_serializers(emp, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status = 204)





