# Generated by Django 4.0.3 on 2022-03-19 11:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelseller',
            name='companyName',
            field=models.CharField(help_text='Şirket İsmi', max_length=150, null=True, verbose_name='Şirket İsmi'),
        ),
        migrations.AlterField(
            model_name='modelseller',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='modelseller',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Telefon', max_length=128, null=True, region=None, verbose_name='Telefon'),
        ),
    ]