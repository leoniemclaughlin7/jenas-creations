# Generated by Django 3.2.23 on 2024-02-11 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]
