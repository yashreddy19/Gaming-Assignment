from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=200)
    url = serializers.URLField()
    author = serializers.CharField(max_length=200)
    published_date = serializers.DateField()

    def validate(self, attrs):
        url = attrs.get("url")
        if Game.objects.filter(url=url).exists():
            raise serializers.ValidationError("A game with this URL already exists.")
        return attrs

    def create(self, validated_data):
        Game.objects.create(**validated_data)
        return validated_data

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
