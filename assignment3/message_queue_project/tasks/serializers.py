from rest_framework import serializers
from .models import SecureModel

class SecureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureModel
        fields = ['id', 'name', 'url']
