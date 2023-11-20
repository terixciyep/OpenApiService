import json

import yaml
from rest_framework import serializers
from openapi.models import OpenApiFile, AllowedHTTPMethods
from openapi.openapi_utils import format_validator

class FileSerializer(serializers.ModelSerializer):
    methods = serializers.ListField(child=serializers.CharField(), required=False)
    class Meta:
        model = OpenApiFile
        fields = ['id','name','file','methods']

    def validate_methods(self, methods):
        if methods is None:
            return methods
        if isinstance(methods, str):
            return [methods]
        if isinstance(methods, list):
            return methods

        return None

    def to_representation(self, instance):
        represantation = super().to_representation(instance)
        data = self.get_methods_openapi(instance.file)
        represantation['methods'] = data
        return represantation

    def get_methods_openapi(self, file):
        file_data = file.read().decode('utf-8')
        extension_allow = format_validator(file_data)
        if not extension_allow:
            raise ValueError('Недопустимый формат файла: только JSON/Yaml ')
        if extension_allow=='json':
            data = json.loads(file_data)
        elif extension_allow=='yaml':
            data = yaml.safe_load(file_data)
        else:
            raise ValueError('Неправильный формат файла')

        if 'paths' not in data:
            return None

        paths = data['paths']
        http_methods = set()

        for path, methods in paths.items():
            http_methods.update(methods.keys())

        return http_methods

class MethodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    method = serializers.ListField(child=serializers.CharField(), required=False)
    class Meta:
        model = OpenApiFile
        fields = ['id','method']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        openapi_file_id = instance.id
        openapi_file = OpenApiFile.objects.get(id=openapi_file_id)
        representation['name'] = openapi_file.name
        methods = openapi_file.allowed_methods.all()  # Получение всех методов для данного OpenApiFile
        representation['methods'] = {}
        for method_instance in methods:
            representation['methods'][method_instance.id] = method_instance.method

        return representation

    def create(self, validated_data):
        methods = validated_data['method']
        openapi_file_id = validated_data['id']

        if isinstance(methods, list):
            instances = []
            for method in methods:
                instance = AllowedHTTPMethods.objects.create(
                    openapi_file_id=openapi_file_id,
                    method=method,
                )
                instances.append(instance)
            return OpenApiFile.objects.get(id=openapi_file_id)
        elif isinstance(methods, str):
            AllowedHTTPMethods.objects.create(
                openapi_file_id=openapi_file_id,
                method=methods,
            )
            return OpenApiFile.objects.get(id=openapi_file_id)
        else:
            return super().create(validated_data)

class AllowedHTTPMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedHTTPMethods
        fields = ('id', 'method')

class OpenApiFileSerializer(serializers.ModelSerializer):
    allowed_methods = AllowedHTTPMethodsSerializer(many=True, read_only=True)

    class Meta:
        model = OpenApiFile
        fields = ('id', 'name', 'file', 'allowed_methods')