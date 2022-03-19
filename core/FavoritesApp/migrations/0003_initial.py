# Generated by Django 4.0.3 on 2022-03-19 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FavoritesApp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelfavorite',
            name='user',
            field=models.ForeignKey(help_text='Kullanıcı', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]