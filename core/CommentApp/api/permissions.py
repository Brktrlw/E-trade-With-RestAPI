from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from OrderApp.models import ModelOrderItems,ModelUser,ModelOrder
from ProductsApp.models import ModelProduct

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAnyOrder(BasePermission):
    message = "Ürünü satın almadığınız için yorum yapamazsınız."

    def has_permission(self, request, view):
        product  = get_object_or_404(ModelProduct,slug=view.kwargs.get("slug"))
        try:
            order  = ModelOrder.objects.get(user=request.user)
        except:
            return False
        isBought = ModelOrderItems.objects.filter(order=order,item=product).exists()
        if isBought:
            return True
        return False


