from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct



class ModelCart(models.Model):
    user      = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı",related_name="cart")

    def __str__(self):
        return self.user.username + "'in sepeti."

    class Meta:
        verbose_name        = "Cart"
        verbose_name_plural = "Carts"
        db_table            = "Cart"

    def getTotalPrice(self):
        totalPrice=0
        prodcts=self.user.cart.first().items.all()
        for product in prodcts:
            totalPrice+=product.product.price
        return totalPrice

class ModelCartItem(models.Model):
    cart    = models.ForeignKey(ModelCart,on_delete=models.CASCADE,verbose_name="Sepet",help_text="Sepet",related_name="items")
    product = models.ForeignKey(ModelProduct,on_delete=models.CASCADE,verbose_name="Ürün",help_text="Ürün")
    amount  = models.IntegerField(verbose_name="Adet",help_text="Adet")


    class Meta:
        verbose_name        = "Cart Item"
        verbose_name_plural = "Cart Items"
        db_table            = "CartItems"





