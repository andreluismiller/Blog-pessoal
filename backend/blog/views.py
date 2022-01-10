from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import PostBlog
from blog.serializers import PostBlogSerializer

#View to list all blog posts
class PostBlogListView(ListAPIView):
    queryset = PostBlog.objects.order_by('-data_criação')
    serializer_class = PostBlogSerializer
    lookup_field = 'slug'
    permissions_classes = (permissions.AllowAny, )

#View to see the details of each blog post
class PostBlogDetailView(RetrieveAPIView):
    queryset = PostBlog.objects.order_by('-data_criação')
    serializer_class = PostBlogSerializer
    lookup_field = 'slug'
    permissions_classes = (permissions.AllowAny, )

class PostBlogFeaturedView(ListAPIView):
    queryset = PostBlog.objects.all().filter(feature=True)
    serializer_class = PostBlogSerializer
    lookup_field = 'slug'
    permissions_classes = (permissions.AllowAny, )

#View to filter blog posts by category
class PostBlogCategoryView(APIView):
    serializer_class = PostBlogSerializer
    permissions_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = PostBlog.objects.order_by('-data_criação').filter(category__iexact=category)

        serializer = PostBlogSerializer(queryset, many=True)

        return Response(serializer.data)