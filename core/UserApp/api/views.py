from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer
from rest_framework import generics
from UserApp.models import ModelUser






class RegisterView(generics.CreateAPIView):
    queryset           = ModelUser.objects.all()
    permission_classes = [AllowAny,]
    serializer_class   = RegisterUserSerializer

