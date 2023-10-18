from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PsytestSerializers

from .models import PsyTest, Question, Answer, Result


# 테스트 만들기
class PsytestView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        serializer = PsytestSerializers(data=request.data)

        if serializer.is_valid():
            psytest_instance = serializer.save()
            psytest_instance.writer = request.user
            psytest_instance.save()

            return Response({'message': 'Psytest가 성공적으로 만들어졌습니다.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 질문 만들기
class QuestionmakeView(APIView):
    permission_classes = [IsAuthenticated]
