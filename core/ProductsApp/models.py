from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from unidecode import unidecode

class ModelProductCategory(models.Model):
    name=models.CharField(max_length=100,verbose_name="Kategori",help_text="Kategori")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Product Category"
        verbose_name_plural = "Product Categories"
        db_table            = "ProductCategories"


class ModelProduct(models.Model):
    name        = models.CharField(max_length=200,verbose_name="Ürün",help_text="Ürün")
    description = models.TextField(max_length=500,verbose_name="Detay",help_text="Detay")
    slug        = AutoSlugField(populate_from="name",unique=True,help_text="Slug",verbose_name="Slug")
    category    = models.ManyToManyField(ModelProductCategory,verbose_name="Kategori",help_text="Kategori",related_name="categs")
    image       = models.ImageField(upload_to="Products",verbose_name="Görsel",help_text="Görsel")
    draft       = models.BooleanField(default=True,verbose_name="Taslak",help_text="Taslak")
    price       = models.FloatField(verbose_name="Fiyat",help_text="Fiyat")

    def __str__(self):
        return f"{self.name} | {self.slug}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(ModelProduct, self).save(*args, **kwargs)

    class Meta:
        verbose_name        = "Product"
        verbose_name_plural = "Products"
        db_table            = "Products"
