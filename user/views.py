from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from .serializers import SigninSerializer, ChangePasswordSerializer, ProfileUpdateSerializer

from .models import RefreshToken 


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
        return {'RefreshToken': data['refresh'],'AccessToken': data['access']}


# 로그인
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 로그아웃
class LogoutView(APIView):
    permissions_classes = [IsAuthenticated]

    def post(self, request):
        request.user.refresh_token.delete()

        return Response({'message': '로그아웃 성공'}, status=status.HTTP_200_OK)
    

# 비밀번호 변경
class ChangePwView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            current_password = serializer.validated_data.get('current_password')
            new_password = serializer.validated_data.get('new_password')

            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': '비밀번호 변경 성공','status':200 },status=status.HTTP_200_OK)
            else:
                return Response({
                    'error_code': status.HTTP_400_BAD_REQUEST,
                    'error': '현재 암호가 틀립니다.'
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
                        'error_code': status.HTTP_400_BAD_REQUEST,
                        'error': serializer.errors['new_password']
                        }, 
                        status=status.HTTP_400_BAD_REQUEST)
    

# 회원 정보 수정
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({
            'error_code': status.HTTP_400_BAD_REQUEST,
            'error': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST)