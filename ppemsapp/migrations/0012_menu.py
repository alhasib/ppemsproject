# Generated by Django 3.1.2 on 2020-12-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppemsapp', '0011_auto_20201128_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
    ]
