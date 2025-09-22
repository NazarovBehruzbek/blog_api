from rest_framework import viewsets,permissions
from .models import Category
from .serializer import CategorySerializer
from drf_spectacular.utils import extend_schema
# Create your views here.
@extend_schema(tags=["Categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]

