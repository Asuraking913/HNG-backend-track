from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

def generate_datetime():

    return datetime.now().isoformat()


# Create your views here.
class CustomView(views.APIView):

    def get(self, *args, **kwargs):

        print(generate_datetime())

        response = {
            "email" : "israelshedrack913@gmail.com", 
            "current_datetime" : str(generate_datetime()),

            "github_url" : "https://github.com/Asuraking913/HNG-backend-track"
        }

        return Response(response, status=status.HTTP_200_OK)