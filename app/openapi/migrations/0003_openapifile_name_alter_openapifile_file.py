# Generated by Django 4.2.6 on 2023-11-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openapi', '0002_remove_openapifile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='openapifile',
            name='name',
            field=models.CharField(default='some', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openapifile',
            name='file',
            field=models.BinaryField(max_length=1000),
        ),
    ]
