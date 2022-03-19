import uuid
from django.db import models
from UserApp.models import ModelUser,ModelAddress
from ProductsApp.models import ModelProduct

class ModelOrder(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı",related_name="orders")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Sipariş Tarihi",help_text="Sipariş Tarihi")
    address     = models.ForeignKey(ModelAddress,on_delete=models.SET_NULL,verbose_name="Adres",help_text="Adres",blank=False,null=True)
    unique_id   = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,verbose_name="Sipariş Id",help_text="Sipariş Id")

    class Meta:
        db_table="Orders"
        verbose_name="Order"
        verbose_name_plural="Orders"

    def __str__(self):
        return f"{self.unique_id}"

class ModelOrderItems(models.Model):
    order  = models.ForeignKey(ModelOrder,on_delete=models.CASCADE,verbose_name="Sipariş",help_text="Sipariş",related_name="items")
    item   = models.ForeignKey(ModelProduct,on_delete=models.CASCADE,verbose_name="Ürün",help_text="Ürün")
    amount = models.PositiveIntegerField(verbose_name="Adet",help_text="Adet")


    def __str__(self):
        return str(self.item.name)

    class Meta:
        verbose_name        = "Order Item"
        verbose_name_plural = "Order Items"
        db_table            = "OrderItems"