# posts/serializers.py
from rest_framework import serializers
from .models import Post
from categories.serializer import CategorySerializer
from comments.serializer import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source="category", read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'created_at',
                  'category', 'category_detail', 'comment_count', 'comments']

    def get_comment_count(self, obj):
        return obj.comments.count()
