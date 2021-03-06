# Generated by Django 4.0.3 on 2022-03-19 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OrderApp', '0002_initial'),
        ('UserApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='modelorder',
            name='address',
            field=models.ForeignKey(help_text='Adres', null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.modeladdress', verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='modelorder',
            name='user',
            field=models.ForeignKey(help_text='Kullanıcı', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
