# Generated by Django 4.0.3 on 2022-03-14 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(help_text='Yorum', max_length=300, verbose_name='Yorum')),
                ('createdDate', models.DateTimeField(auto_now_add=True, help_text='Oluşturma Tarihi', verbose_name='Oluşturma Tarihi')),
                ('modifiedDate', models.DateTimeField(auto_now=True, help_text='Düzenleme Tarihi', verbose_name='Düzenleme Tarihi')),
                ('product', models.ForeignKey(help_text='Ürün', on_delete=django.db.models.deletion.CASCADE, to='ProductsApp.modelproduct', verbose_name='Ürün')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'Comments',
            },
        ),
    ]