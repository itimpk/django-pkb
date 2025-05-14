# notes/serializers.py

from rest_framework import serializers
from .models import Note
from taggit.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'tags', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Extract the new tags
        tags_data = validated_data.pop('tags', None)

        # Update the instance with other validated data
        instance = super().update(instance, validated_data)

        if tags_data is not None:
            # Clear existing tags
            instance.tags.clear()

            # Add new tags
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)

        return instance
