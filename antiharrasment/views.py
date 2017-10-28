from django.shortcuts import render
from django.http import JsonResponse
from .models import query
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuerySerializer

from .nlp import pred

# Create your views here.
@api_view(['POST'])
def get_is_harassing(request):
    return Response({"is_harassing": pred(request.data.get("statement"))})

@api_view(['POST'])
def add_query(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
