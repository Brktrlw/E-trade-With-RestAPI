from django.db import models
from UserApp.models import ModelUser


class ModelSeller(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete = models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı")
    companyName = models.CharField(max_length=150,verbose_name="Şirket İsmi",help_text="Şirket İsmi")


    def __str__(self):
        return f"{self.companyName}"

    class Meta:
        verbose_name        = "Seller"
        verbose_name_plural = "Sellers"
        db_table            = "Sellers"
