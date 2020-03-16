from rest_framework import serializers
from .models import Test, Questions

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'title']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['title', 'question', 'a1', 'a2','a3','a4']