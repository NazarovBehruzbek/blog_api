from rest_framework import viewsets
from .models import Comment
from .serializer import CommentSerializer
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

@extend_schema(tags=["Comments"])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post_id']
