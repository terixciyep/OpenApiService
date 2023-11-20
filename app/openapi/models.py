from django.db import models


class OpenApiFile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='openapi_files')

class AllowedHTTPMethods(models.Model):
    openapi_file = models.ForeignKey(to=OpenApiFile, on_delete=models.CASCADE, related_name='allowed_methods')
    method = models.CharField(max_length=255)