# Generated by Django 3.2.23 on 2024-02-26 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_default_full_name'),
        ('custom_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
            preserve_default=False,
        ),
    ]
