from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from UserApp.models import ModelUser
from SellerApp.models import ModelSeller


@receiver(post_save,sender=ModelUser)
def whenCreateUser(sender,instance,created,*args,**kwargs):
    # When create order then create cart for that user
    if created:
        if instance.isCustomer:
            ModelCart=apps.get_model('CartApp.ModelCart')
            ModelCart.objects.create(user=instance)
        else:
            ModelSeller.objects.create(user=instance)


