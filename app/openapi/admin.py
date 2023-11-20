from django.contrib import admin

from openapi.models import OpenApiFile, AllowedHTTPMethods

admin.site.register(OpenApiFile)
admin.site.register(AllowedHTTPMethods)