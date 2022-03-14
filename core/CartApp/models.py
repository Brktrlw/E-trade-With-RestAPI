from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct

class ModelCart(models.Model):
    user      = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı")

    def __str__(self):
        return self.user.username


class ModelCartItem(models.Model):
    cart   = models.ForeignKey(ModelCart,on_delete=models.CASCADE,verbose_name="Sepet",help_text="Sepet")
    item   = models.ForeignKey(ModelProduct,on_delete=models.CASCADE,verbose_name="Ürün",help_text="Ürün")
    amount = models.IntegerField(verbose_name="Adet",help_text="Adet")

    class Meta:
        verbose_name        = "Cart Item"
        verbose_name_plural = "Cart Items"
        db_table            = "CartItems"
