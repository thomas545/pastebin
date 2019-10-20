from rest_framework import serializers

from .models import Paste


class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        exclude = ['user']

        
class PasteMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        exclude = ['created', 'modified']