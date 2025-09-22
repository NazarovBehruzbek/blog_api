from rest_framework import viewsets,permissions,generics
from .models import User
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from rest_framework.exceptions import AuthenticationFailed as DRFAuthFailed

@extend_schema_view(
    post=extend_schema(tags=["Users"])
)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except (AuthenticationFailed, InvalidToken, DRFAuthFailed):
            raise AuthenticationFailed("Username or password is incorrect")


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer