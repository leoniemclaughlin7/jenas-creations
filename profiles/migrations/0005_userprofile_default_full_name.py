# Generated by Django 3.2.23 on 2024-02-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_rename_userprofile_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
