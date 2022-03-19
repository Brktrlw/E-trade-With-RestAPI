# Generated by Django 4.0.3 on 2022-03-19 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductsApp', '0001_initial'),
        ('FavoritesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelfavorite',
            name='product',
            field=models.ForeignKey(help_text='Ürün', on_delete=django.db.models.deletion.CASCADE, to='ProductsApp.modelproduct', verbose_name='Ürün'),
        ),
    ]
