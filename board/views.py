from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from ipware import get_client_ip
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
        serializer = PostSerializer(data=request.data)
        ip = get_client_ip(request)
        if serializer.is_valid():
            post = serializer.save(author=ip)
            serializer = PostSerializer(post).data
            return Response(data=serializer, status=status.HTTP_200_OK)
        else:
            error_msg = serializer.errors
            return Response(data=error_msg, status=status.HTTP_400_BAD_REQUEST)


