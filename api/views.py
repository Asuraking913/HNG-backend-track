from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .utils import handle_perfect, handle_prime, handle_properties, handle_sum
from .service import NumberAPISerivice

def generate_datetime():

    return datetime.utcnow().isoformat(timespec='seconds') + 'Z'




# Create your views here.
class CustomView(views.APIView):

    def get(self, *args, **kwargs):


        response = {
            "message" : "Stage Two Task",

            "github_url" : "https://github.com/Asuraking913/HNG-backend-track"
        }

        return Response(response, status=status.HTTP_200_OK)
    
class HandleNumberView(views.APIView):

    def get(self, request):

        api_class = NumberAPISerivice()

        try:
            number = int(request.query_params.get('number'))

            is_prime = handle_prime(number)
            is_perfect = handle_perfect(number)
            properties = handle_properties(number)
            digit_sum = handle_sum(number)
            
            response_text = api_class.get_fun_fact(number)


            response = {
            "number" : number, 
            "is_prime" : is_prime,
            "is_perfect" : True if is_perfect == number else False, 
            "properties" : properties,
            "digit_sum" : digit_sum, 
            "fun_fact" : f"{response_text}"
            }
            
            return Response(response)

        except ValueError:
            response = {
                "number" : "alphabet", 
                "error" : "true"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
