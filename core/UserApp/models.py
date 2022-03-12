from django.db import models
from django.contrib.auth.models import AbstractUser
import json

with open('fixtures/city.json') as f:
    cities = json.load(f)
cities = [(k, v) for k, v in cities.items()]

class ModelAddress(models.Model):
    name    = models.CharField(max_length=50,verbose_name="Adres Başlığı",help_text="Adres Başlığı")
    city    = models.CharField(choices=cities,max_length=20,verbose_name="Şehir",help_text="Şehir")
    street  = models.CharField(max_length=150,verbose_name="Sokak",help_text="Sokak")
    address = models.TextField(max_length=500,verbose_name="Açık Adres",help_text="Açık Adres")

    def __str__(self):
        return self.name

class ModelUser(AbstractUser):
    avatar = models.ImageField(upload_to="Users",verbose_name="Profil Fotoğrafı",help_text="Profil Fotoğrafı",null=True,blank=True)
    address= models.ManyToManyField(ModelAddress,verbose_name="Adresler",help_text="Adresler",blank=True,related_name="addrs")

    class Meta:
        verbose_name        = "User"
        verbose_name_plural = "Users"
        db_table            = "Users"