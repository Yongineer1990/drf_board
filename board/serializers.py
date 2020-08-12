from rest_framework import serializers

import jwt

from drf_board.settings import (
    SECRET_KEY,
    ALGORITHM
)
from .models import (
    Post,
    Comment,
    Reply
)

class PostSerializer(serializers.ModelSerializer):
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

class ReplySerializer(serializers.ModelSerializer):

    post = PostSerializer()

    class Meta:
        model = Reply
        exclude = ()
        read_only_fields = (
            'id',
            'password',
            'created_at',
            'updated_at',
        )
