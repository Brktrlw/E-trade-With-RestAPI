# Generated by Django 4.0.3 on 2022-03-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelproduct',
            name='category',
            field=models.ManyToManyField(help_text='Kategori', related_name='categs', to='ProductsApp.modelproductcategory', verbose_name='Kategori'),
        ),
    ]
