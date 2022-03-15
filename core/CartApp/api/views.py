from rest_framework.generics import CreateAPIView, get_object_or_404,DestroyAPIView,UpdateAPIView
from CartApp.models import ModelCart,ModelCartItem
from .serializers import CartSerializer
from ProductsApp.models import ModelProduct
from rest_framework.permissions import IsAuthenticated

class AddProductToCartView(CreateAPIView):
    queryset           = ModelCartItem.objects.all()
    serializer_class   = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        #If there is the same product in the cart of customer , then increase amount.
        cart    = get_object_or_404(ModelCart,user=self.request.user)
        product = get_object_or_404(ModelProduct,slug=self.kwargs.get("slug"),draft=False)
        cartItem= ModelCartItem.objects.filter(cart=cart,item=product)
        if cartItem:
            cartItem[0].amount=cartItem[0].amount+serializer.validated_data.get("amount")
            cartItem[0].save()
        else:
            serializer.save(cart=cart,item=product)


class ReduceProductFromCartView(DestroyAPIView):
    queryset         = ModelCartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        product  = get_object_or_404(ModelProduct, slug=self.kwargs.get("slug"),draft=False)
        return product

    def perform_destroy(self, instance):
        cart     = get_object_or_404(ModelCart,user=self.request.user)
        product  = self.get_object()
        cartItem = get_object_or_404(ModelCartItem,cart=cart, item=product)
        if cartItem.amount==1:
            cartItem.delete()
        else:
            cartItem.amount-=1
            cartItem.save()


class DeleteProductFromCartView(DestroyAPIView):
    queryset = ModelCartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        product = get_object_or_404(ModelProduct, slug=self.kwargs.get("slug"),draft=False)
        return product

    def perform_destroy(self, instance):
        cart     = get_object_or_404(ModelCart,user=self.request.user)
        product  = self.get_object()
        cartItem = get_object_or_404(ModelCartItem,cart=cart, item=product)
        cartItem.delete()


class UpdateCartItemAmountView(UpdateAPIView):

    queryset         = ModelCartItem.objects.all()
    serializer_class = CartSerializer

    def get_cart_product_cartItem(self):
        cart     = get_object_or_404(ModelCart, user=self.request.user)
        product  = get_object_or_404(ModelProduct, slug=self.kwargs.get("slug"))
        cartItem = get_object_or_404(ModelCartItem, cart=cart, item=product)
        return {"cart":cart,"product":product,"cartItem":cartItem}

    def get_object(self):
        return self.get_cart_product_cartItem().get("cartItem")

    def perform_update(self, serializer):
        cartItem = self.get_cart_product_cartItem().get("cartItem")

        if serializer.validated_data.get("amount")==0:
            cartItem.delete()
        elif serializer.validated_data.get("amount")<0:
            return ValueError("0dan küçük olamaz.")
        else:
            cartItem.amount=serializer.validated_data.get("amount")
            cartItem.save()







