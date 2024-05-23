from rest_framework import serializers

from .models import *


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = ['variants']


class QuestionSerializer(serializers.ModelSerializer):
    variants = VariantsSerializer(source='variants_id')

    class Meta:
        model = Question
        fields = ['id', 'question_name', 'level', 'correct_answer', 'variants']
