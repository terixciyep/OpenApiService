# Generated by Django 4.2.6 on 2023-11-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openapi', '0003_openapifile_name_alter_openapifile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openapifile',
            name='file',
            field=models.FileField(upload_to='openapi_files'),
        ),
    ]
