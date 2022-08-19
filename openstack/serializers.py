from rest_framework import serializers
from .models import OpenstackInstance

class OpenstackInstanceSerializer(serializers.Serializer):
    flavor_id = serializers.CharField()
    volume_size = serializers.IntegerField()

    class Meta:
        model = OpenstackInstance
        fields = ['flavor_id', 'volume_size']