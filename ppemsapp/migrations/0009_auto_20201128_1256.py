# Generated by Django 3.1.2 on 2020-11-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppemsapp', '0008_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='si.png', null=True, upload_to=''),
        ),
    ]
