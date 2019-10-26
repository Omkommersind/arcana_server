from django.http import JsonResponse
from djangorestframework_camel_case.util import camelize
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from arcana_server.settings import DEFAULT_LANGUAGE_CODE
from arcana_server.utils import get_body_in_request
from main.mappers import RequestToCategoriesMapper
from main.repositories import CategoryRepository, QuestionRepository
from main.serializers import CategorySerializer, QuestionSerializer


class Test(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        return Response('PING', status=200)


class Categories(APIView):
    permission_classes = AllowAny,

    @staticmethod
    def get(request):
        language_code = request.META.get('HTTP_LANGUAGE', DEFAULT_LANGUAGE_CODE).lower()
        categories = CategoryRepository.get_all_categories()
        return Response(camelize(CategorySerializer(categories, context={'language_code': language_code}, many=True).data), status=200)


class RandomQuestion(APIView):
    permission_classes = AllowAny,

    @staticmethod
    def get(request):
        language_code = request.META.get('HTTP_LANGUAGE', DEFAULT_LANGUAGE_CODE).lower()
        categories = RequestToCategoriesMapper.map(request.query_params)
        question = QuestionRepository.get_random_question(categories)
        return Response(camelize(QuestionSerializer(question, context={'language_code': language_code}).data), status=200)
