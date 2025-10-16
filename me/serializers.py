from rest_framework import serializers

class MySerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    stack = serializers.CharField(max_length=100)