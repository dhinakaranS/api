from django.shortcuts import render
from .models import employee
from .serializers import emp_serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
def emp(request):
    if request.method == 'GET':    
        queryset = employee.objects.all()
        serializer = emp_serializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

