from django.db.models.signals import post_save
from django.dispatch import receiver
from OrderApp.models import ModelOrder,ModelOrderItems



@receiver(post_save,sender=ModelOrder)
def whenCreateOrder(sender,instance,created,*args,**kwargs):
    user      = instance.user
    cartItems = user.cart.first().items.all()

    for item in cartItems:
        ModelOrderItems.objects.create(order=instance,item=item.item,amount=item.amount)
        item.delete()
