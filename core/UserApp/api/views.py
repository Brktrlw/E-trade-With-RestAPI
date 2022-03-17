from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import RegisterUserSerializer
from rest_framework.generics import CreateAPIView,DestroyAPIView
from UserApp.models import ModelUser


class RegisterUserView(CreateAPIView):
    queryset           = ModelUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class   = RegisterUserSerializer


class DeleteUserView(DestroyAPIView):
    queryset           = ModelUser.objects.all()
    serializer_class   = RegisterUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
