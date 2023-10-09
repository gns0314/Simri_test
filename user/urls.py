from django.urls import path
from .views import SigninView, MyTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('signin/', SigninView.as_view(), name='signin'),
    # 로그인
    path('login/',  MyTokenObtainPairView.as_view(), name='login'),
    # 토큰 재발급
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 로그아웃
    path('logout/',  LogoutView.as_view(), name='logout'),
    
]