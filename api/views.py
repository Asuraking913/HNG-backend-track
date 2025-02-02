from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .utils import handle_perfect, handle_prime, handle_properties

def generate_datetime():

    return datetime.utcnow().isoformat(timespec='seconds') + 'Z'




# Create your views here.
class CustomView(views.APIView):

    def get(self, *args, **kwargs):

        print(generate_datetime())

        response = {
            # "email" : "israelshedrack913@gmail.com", 
            # "current_datetime" : str(generate_datetime()),
            "message" : "Stage Two Task",

            "github_url" : "https://github.com/Asuraking913/HNG-backend-track"
        }

        return Response(response, status=status.HTTP_200_OK)
    
class HandleNumberView(views.APIView):

    def get(self, request):


        try:
            number = int(request.query_params.get('number'))
            # is_prime = False

            is_prime = handle_prime(number)
            is_perfect = handle_perfect(number)
            properties = handle_properties(number)
            print(properties)


            response = {
            "number" : 371, 
            "is_prime" : is_prime,
            "is_perfect" : True if is_perfect == number else False, 
            "properties" : ['armstrong', "odd"],
            "digit_sum" : 11, 
            "fun_fact" : "371"
            }
            
            return Response({"msg" : response})

        except ValueError:
            return Response({"msg" : "testing"})
