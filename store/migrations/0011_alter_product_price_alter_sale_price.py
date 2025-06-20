# Generated by Django 5.1.7 on 2025-03-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
