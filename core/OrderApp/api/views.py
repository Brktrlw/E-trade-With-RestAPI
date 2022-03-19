from rest_framework.generics import CreateAPIView,ListAPIView
from OrderApp.models import ModelOrder,ModelOrderItems
from .serializers import OrderSerializer,OrderListSerializer,OrderItemListSerializer
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


class OrderItemsListAPIView(ListAPIView):
    serializer_class   = OrderItemListSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        return ModelOrderItems.objects.filter(order__unique_id=self.kwargs.get("unique_id"),order__user=self.request.user)










