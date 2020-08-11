from rest_framework import serializers
from .models import (
    Post,
    Comment,
    Reply
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = (
            'body',
            'password',
            'comment',
        )

    def validate(self, data):
        if len(data.get('password')) > 5:
            raise serializers.ValidationError('INVALID PASSWORD')
        return data



