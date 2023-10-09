from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import SigninSerializer

from .models import RefreshToken 

from django.contrib.auth import get_user_model

User = get_user_model()



# 회원가입
class SigninView(APIView):
    def post(self, request):
        serializer = SigninSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공'}, status=status.HTTP_201_CREATED)
        
        return Response({'error_code': status.HTTP_400_BAD_REQUEST},status= status.HTTP_400_BAD_REQUEST)
    

# 로그인 성공시 토큰 발급
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        refresh_token, _ = RefreshToken.objects.get_or_create(user=self.user)
        refresh_token.token = str(refresh)
        refresh_token.save()
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
