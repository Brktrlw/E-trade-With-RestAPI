# Generated by Django 4.0.3 on 2022-03-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsApp', '0002_alter_modelproductcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelproduct',
            name='category',
            field=models.ManyToManyField(help_text='Kategori', related_name='categs', to='ProductsApp.modelproductcategory', verbose_name='Kategori'),
        ),
    ]
