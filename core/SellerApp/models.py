from django.db import models
from UserApp.models import ModelUser
from phonenumber_field.modelfields import PhoneNumberField


class ModelSeller(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete = models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı")
    companyName = models.CharField(max_length=150,verbose_name="Şirket İsmi",help_text="Şirket İsmi",null=True)
    phone       = PhoneNumberField(help_text="Telefon",verbose_name="Telefon",null=True)
    website     = models.URLField(max_length=300,verbose_name="Site",help_text="Site",null=True,blank=True)

    def __str__(self):
        return f"{self.companyName}"

    class Meta:
        verbose_name        = "Seller"
        verbose_name_plural = "Sellers"
        db_table            = "Sellers"
