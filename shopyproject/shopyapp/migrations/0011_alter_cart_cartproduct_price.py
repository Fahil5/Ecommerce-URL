# Generated by Django 4.1.7 on 2023-04-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyapp', '0010_alter_cart_cartproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_price',
            field=models.IntegerField(default='true'),
        ),
    ]
