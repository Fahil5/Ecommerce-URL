# Generated by Django 4.1.7 on 2023-04-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyapp', '0009_alter_cart_cartproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_price',
            field=models.IntegerField(default='True'),
        ),
    ]
