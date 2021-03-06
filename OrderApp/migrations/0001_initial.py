# Generated by Django 4.0.3 on 2022-03-19 10:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True, help_text='Sipariş Tarihi', verbose_name='Sipariş Tarihi')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Sipariş Id', unique=True, verbose_name='Sipariş Id')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='ModelOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(help_text='Adet', verbose_name='Adet')),
                ('price', models.PositiveIntegerField(help_text='Fiyat', verbose_name='Fiyat')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'db_table': 'OrderItems',
            },
        ),
    ]
