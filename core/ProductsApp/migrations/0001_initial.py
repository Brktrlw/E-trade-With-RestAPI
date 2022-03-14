# Generated by Django 4.0.3 on 2022-03-14 15:07

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelProductCategory',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, help_text='Slug', populate_from='name', primary_key=True, serialize=False, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
                'db_table': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='ModelProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, help_text='Slug', populate_from='name', unique=True, verbose_name='Slug')),
                ('description', models.TextField(help_text='Detay', max_length=500, verbose_name='Detay')),
                ('image', models.ImageField(blank=True, help_text='Görsel', null=True, upload_to='Products', verbose_name='Görsel')),
                ('draft', models.BooleanField(default=True, help_text='Taslak', verbose_name='Taslak')),
                ('price', models.FloatField(help_text='Fiyat', verbose_name='Fiyat')),
                ('category', models.ManyToManyField(help_text='Kategori', related_name='categs', to='ProductsApp.modelproductcategory', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Products',
            },
        ),
    ]
