from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializer import  PostSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.

@extend_schema(tags=["Posts"])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

