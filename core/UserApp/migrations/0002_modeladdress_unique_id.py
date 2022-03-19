# Generated by Django 4.0.3 on 2022-03-19 06:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeladdress',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Adres Id', unique=True, verbose_name='Adres ID'),
        ),
    ]
