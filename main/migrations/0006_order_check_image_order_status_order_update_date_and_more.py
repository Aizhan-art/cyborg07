# Generated by Django 5.1.6 on 2025-03-11 04:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_paymentmethod'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='check_image',
            field=models.ImageField(default=1, upload_to='media/check', verbose_name='Чек'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_processing', 'В обработке'), ('denied', 'Отклонено'), ('accepted', 'Принято')], default='in_processing', max_length=15, verbose_name='Статус оплаты'),
        ),
        migrations.AddField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
