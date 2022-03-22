from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status
import requests

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({"message": "welcome to email service"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def sendmail(request):
    data = request.data

    email = Email.objects.create(
        email = data['email'],
        username = data["username"]
    ) 


    return Response({"message": "email sent successfully"}, status=status.HTTP_200_OK)