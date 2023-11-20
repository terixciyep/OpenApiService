from rest_framework import generics, mixins
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django import forms
from rest_framework.viewsets import GenericViewSet

from openapi.models import OpenApiFile, AllowedHTTPMethods
from openapi.openapi_utils import format_validator
from openapi.serializers import FileSerializer, MethodsSerializer, OpenApiFileSerializer


class FilesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = OpenApiFile.objects.all()
    serializer_class = FileSerializer

class AllowedHTTPMethodsViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                GenericViewSet):
    queryset = AllowedHTTPMethods.objects.all()
    serializer_class = MethodsSerializer

class FileDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OpenApiFileSerializer
    queryset = OpenApiFile.objects.all()
    lookup_field = 'pk'


