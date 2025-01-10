from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .services import get_weather_data
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def weather_view(request):
    city = request.GET.get("city", "London")  # Default city is London
    result = get_weather_data(city)
    
    if result["success"]:
        return Response(result["data"])
    else:
        return Response({"error": result["error"]}, status=400)


# @api_view(["GET"])
# def weather_view(request):
#     city = request.GET.get("city", "London")
#     result = get_weather_data(city)
    
#     if result["success"]:
#         return Response(result["data"])
#     else:
#         return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def weather_view(request):
#     city = request.GET.get("city", "London")
#     result = get_weather_data(city)
    
#     if result["success"]:
#         return Response(result["data"])
#     else:
#         return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)