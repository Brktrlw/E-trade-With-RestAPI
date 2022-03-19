from rest_framework.generics import CreateAPIView
from OrderApp.models import ModelOrder,ModelOrderItems
from .serializers import OrderSerializer

class CreateOrderAPIView(CreateAPIView):
    queryset         = ModelOrder.objects.all()
    serializer_class = OrderSerializer


    def perform_create(self, serializer):
        user        = self.request.user
        serializer.save(user=user)









