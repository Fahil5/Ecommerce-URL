# Generated by Django 4.1.7 on 2023-04-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyapp', '0002_remove_category_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
