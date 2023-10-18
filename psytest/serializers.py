from rest_framework import serializers

from .models import PsyTest


# 테스트 창
class PsytestSerializers(serializers.ModelSerializer):

    class Meta:
        model = PsyTest
        fields = '__all__'