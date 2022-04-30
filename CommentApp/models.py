import uuid
from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct
from django.utils.encoding import smart_str


class ModelComment(models.Model):
    unique_id    = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user         = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",help_text="Kullanıcı")
    product      = models.ForeignKey(ModelProduct,on_delete=models.CASCADE,verbose_name="Ürün",help_text="Ürün")
    comment      = models.TextField(max_length=300,verbose_name="Yorum",help_text="Yorum")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi",help_text="Oluşturma Tarihi")
    modifiedDate = models.DateTimeField(auto_now=True,verbose_name="Düzenleme Tarihi",help_text="Düzenleme Tarihi")

    def __str__(self):
        return smart_str(f"{self.user} | {self.comment}")

    class Meta:
        verbose_name        = "Comment"
        verbose_name_plural = "Comments"
        db_table            = "Comments"


