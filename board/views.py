from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from ipware import get_client_ip
import bcrypt

from drf_board.settings import (
    SECRET_KEY,
    ALGORITHM
)
from .serializers import PostSerializer
from .models import Post

class Pagination(PageNumberPagination):
        page_size = 5

class PostView(APIView):

    def get(self, request):
        paginator = Pagination()
        posts = Post.objects.all()
        results = paginator.paginate_queryset(posts, request)
        serializers = PostSerializer(results, many=True).data
        return paginator.get_paginated_response(serializers)

    def post(self, request):
        ip = get_client_ip(request)
        hashed_password = bcrypt.hashpw(request.data['password'].encode('utf-8'), bcrypt.gensalt())
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(author=ip, password=hashed_password)
            serializer = PostSerializer(post).data
            return Response(data=serializer, status=status.HTTP_200_OK)
        else:
            error_msg = serializer.errors
            return Response(data=error_msg, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def get_post(self, postid):
        try:
            post = Post.objects.get(id=postid)
            return post
        except Post.DoesNotExist:
            return None

    def get(self, request, postid):
        post = self.get_post(postid)
        if post is not None:
            serializer = PostSerializer(post).data
            return Response(data=serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, postid):
        post = self.get_post(postid)
        if post is not None:
            if not bcrypt.checkpw(request.data['password'].encode('utf-8'), post.password):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                post = serializer.save()
                return Response(PostSerializer(post).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, postid):
        post = self.get_post(postid)
        if post is not None:
            if not bcrypt.checkpw(request.data['password'].encode('utf-8'), post.password):
                return Response(status=status.HTTP_403_FORBIDDEN)
            post.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
