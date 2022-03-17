from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct


class ModelFavorite(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı")
    product     = models.ForeignKey(ModelProduct,on_delete=models.CASCADE,verbose_name="Ürün",help_text="Ürün")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Kaydetme Tarihi",help_text="Kaydetme Tarihi")

    class Meta:
        verbose_name        = "Favorite"
        verbose_name_plural = "Favorites"
        db_table            = "Favorites"

    def __str__(self):
        return f"{self.user.username}'in {self.product.name} favorisi"
