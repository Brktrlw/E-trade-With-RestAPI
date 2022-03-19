# Generated by Django 4.0.3 on 2022-03-19 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CartApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcart',
            name='user',
            field=models.ForeignKey(help_text='Kullanıcı', on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='modelcartitem',
            name='cart',
            field=models.ForeignKey(help_text='Sepet', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='CartApp.modelcart', verbose_name='Sepet'),
        ),
    ]
