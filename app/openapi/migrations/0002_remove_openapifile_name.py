# Generated by Django 4.2.6 on 2023-11-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openapifile',
            name='name',
        ),
    ]