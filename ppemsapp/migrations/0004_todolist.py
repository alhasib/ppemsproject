# Generated by Django 3.1.2 on 2020-11-14 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ppemsapp', '0003_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_to_do', models.TextField(blank=True, null=True)),
                ('when_to_do', models.DateField(blank=True, null=True)),
                ('pending_status', models.BooleanField(default=1)),
                ('working_status', models.BooleanField(default=0)),
                ('done_status', models.BooleanField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
