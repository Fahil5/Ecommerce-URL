# Generated by Django 4.1.7 on 2023-04-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyapp', '0006_remove_category_slug_remove_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_image',
            field=models.ImageField(blank=True, default='false', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_name',
            field=models.CharField(default='false', max_length=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_price',
            field=models.IntegerField(default='false'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_quantity',
            field=models.IntegerField(default='false'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartproduct_username',
            field=models.CharField(default='false', max_length=50),
        ),
    ]
