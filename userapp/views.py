from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from userapp.models import User
from userapp.serializers import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


@api_view(['GET'])
def get_user(request, pk):
    # Find User by pk (id)
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'This user does not exist '}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
