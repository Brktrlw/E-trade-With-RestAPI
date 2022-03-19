# Generated by Django 4.0.3 on 2022-03-19 10:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(help_text='Şirket İsmi', max_length=150, verbose_name='Şirket İsmi')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Telefon', max_length=128, region=None, verbose_name='Telefon')),
                ('website', models.URLField(blank=True, help_text='Site', max_length=300, null=True, verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
                'db_table': 'Sellers',
            },
        ),
    ]
