from rest_framework.generics import CreateAPIView,ListAPIView
from OrderApp.models import ModelOrder,ModelOrderItems
from .serializers import OrderSerializer,OrderListSerializer,OrderItemListSerializer
from rest_framework.permissions import IsAuthenticated
from fixtures.bank import Payment


class CreateOrderAPIView(CreateAPIView):
    queryset           = ModelOrder.objects.all()
    serializer_class   = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user        = self.request.user
        if user.cart.first().items.all():
            # For PAYMENT
            totalPrice = user.cart.first().getTotalPrice()
            firstName  = serializer.validated_data.get("payment").get("firstName")
            lastName   = serializer.validated_data.get("payment").get("lastName")
            cardNumber = serializer.validated_data.get("payment").get("cardNumber")
            CVV        = serializer.validated_data.get("payment").get("CVV")
            month      = serializer.validated_data.get("payment").get("month")
            year       = serializer.validated_data.get("payment").get("year")

            checkPayment = Payment(firstName,lastName,cardNumber,CVV,month,year,totalPrice)

            if checkPayment:
                # Payment Success
                serializer.save(user=user)
            else:
                # Payment error
                return ValueError("Bankanız ödemeyi onaylamadı")
        else:
            #if cart is empty
            return ValueError("Sepetiniz Boş")


class ListOrdersAPIView(ListAPIView):
    serializer_class   = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ModelOrder.objects.filter(user=self.request.user)


class OrderItemsListAPIView(ListAPIView):
    serializer_class   = OrderItemListSerializer
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ModelOrderItems.objects.filter(order__unique_id=self.kwargs.get("unique_id"),order__user=self.request.user)










