# Generated by Django 5.1.6 on 2025-03-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_order_paymentrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=225, verbose_name='Покупатель')),
                ('product', models.CharField(max_length=225, verbose_name='Продукт')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('check_image', models.ImageField(upload_to='media/check', verbose_name='Чек')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
    ]
