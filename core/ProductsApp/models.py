from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from unidecode import unidecode
from SellerApp.models import ModelSeller

class BaseProductModel(models.Model):
    # Created a base class to avoid code duplication
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name",unique=True,help_text="Slug",verbose_name="Slug")

    class Meta:
        abstract=True

class ModelProductCategory(BaseProductModel):
    # The two fields (name and slug) come from the inherited (BaseProductModel) class.
    slug = AutoSlugField(populate_from="name",unique=True,help_text="Slug",verbose_name="Slug",primary_key=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nameField = self._meta.get_field('name')
        nameField.verbose_name = 'Kategori Adı'
        nameField.help_text    = "Kategori Adı"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Product Category"
        verbose_name_plural = "Product Categories"
        db_table            = "ProductCategories"


class ModelProduct(BaseProductModel):
    # The two fields (name and slug) come from the inherited (BaseProductModel) class.
    description = models.TextField(max_length=500,verbose_name="Detay",help_text="Detay")
    category    = models.ManyToManyField(
        ModelProductCategory,
        verbose_name="Kategori",
        help_text="Kategori",
        related_name="categs",
    )
    image    = models.ImageField(upload_to="Products",verbose_name="Görsel",help_text="Görsel",blank=True,null=True)
    draft    = models.BooleanField(default=True,verbose_name="Taslak",help_text="Taslak")
    price    = models.FloatField(verbose_name="Fiyat",help_text="Fiyat")
    seller   = models.ForeignKey(ModelSeller,on_delete=models.CASCADE,verbose_name="Mağaza",help_text="Mağaza",related_name="products")
    shipping = models.BooleanField(default=True,verbose_name="Kargo",help_text="Kargo")

    def __str__(self):
        return f"{self.name} | {self.slug}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(ModelProduct, self).save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nameField = self._meta.get_field('name')
        nameField.verbose_name = 'Ürün Adı'
        nameField.help_text    = "Ürün Adı"

    class Meta:
        verbose_name        = "Product"
        verbose_name_plural = "Products"
        db_table            = "Products"
