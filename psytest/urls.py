from django.urls import path
from .views import PsytestView

app_name = 'psytest'

urlpatterns = [
    # 테스트 만들기
    path('make/', PsytestView.as_view(), name='make'),
    
]