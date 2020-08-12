from rest_framework import serializers

from drf_board.settings import (
    SECRET_KEY,
    ALGORITHM
)
from .models import (
    Post,
    Reply
)

class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        exclude = ()
        read_only_fields = (
            'id',
            'password',
            'created_at',
            'updated_at',
            'post',
        )

    def validate(self, data):
        ip = data.get('author')

        if ip == '0.0.0.0':
            raise serializers.ValidationError('Wrong IP')

        return data

class PostSerializer(serializers.ModelSerializer):

    reply = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ()
        read_only_fields = (
            'id',
            'password',
            'created_at',
            'updated_at',
        )

        def validate(self, data):
            ip = data.get('author')

            if ip == '0.0.0.0':
                raise serializers.ValidationError('Wrong IP')

            return data


