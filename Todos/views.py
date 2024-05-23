from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from Todos.models import *
from Todos.serializers import *


class QuestionViewSet(APIView):
    def get(self, request):
        questions = Question.objects.all()
        questions_serializers = QuestionSerializer(questions, many=True).data

        data = {'questions': questions_serializers}

        return Response(data)