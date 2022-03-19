from rest_framework.generics import CreateAPIView
from OrderApp.models import ModelOrder
from .serializers import OrderSerializer

class CreateOrderAPIView(CreateAPIView):
    queryset         = ModelOrder.objects.all()
    serializer_class = OrderSerializer


    def perform_create(self, serializer):
        user        = self.request.user
        if user.cart.first().items.all():
            serializer.save(user=user)
        else:
            #if cart is empty
            raise ValueError("Cart is empty")









