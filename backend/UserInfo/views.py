from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserInfo

class RegisterView(APIView):
    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Getuser(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

