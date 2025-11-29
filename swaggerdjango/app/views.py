from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def first_view(request):
    return Response("First API Developed")



class Second(APIView):
    def get(self, request):
        return Response("Second API Developed")