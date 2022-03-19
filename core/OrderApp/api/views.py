from rest_framework.generics import CreateAPIView,ListAPIView
from OrderApp.models import ModelOrder
from .serializers import OrderSerializer,OrderListSerializer
from rest_framework.permissions import IsAuthenticated


class CreateOrderAPIView(CreateAPIView):
    queryset           = ModelOrder.objects.all()
    serializer_class   = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user        = self.request.user
        if user.cart.first().items.all():
            serializer.save(user=user)
        else:
            #if cart is empty
            raise ValueError("Cart is empty")


class ListOrdersAPIView(ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return ModelOrder.objects.filter(user=self.request.user)










