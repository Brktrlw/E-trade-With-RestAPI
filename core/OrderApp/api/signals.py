from django.db.models.signals import post_save
from django.dispatch import receiver
from OrderApp.models import ModelOrder,ModelOrderItems



@receiver(post_save,sender=ModelOrder)
def whenCreateOrder(sender,instance,created,*args,**kwargs):
    
    print(sender) #order objesi
    print(type(instance)) #oluşan objenin IDsi
    print(created)
        #user_profile=ProfileModel(user=user)
        #   user_profile.save()
    #post_save.connect(whenCreateOrder,sender=ModelOrder)