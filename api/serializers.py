from rest_framework import serializers
from .models import *

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = '__all__'