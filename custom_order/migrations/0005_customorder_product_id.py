# Generated by Django 3.2.23 on 2024-02-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_order', '0004_remove_customorder_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='product_id',
            field=models.IntegerField(default=1000),
        ),
    ]