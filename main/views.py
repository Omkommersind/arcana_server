import uuid as uuid
from django.http import JsonResponse
from djangorestframework_camel_case.util import camelize
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from arcana_server.errors.errors import Errors
from arcana_server.errors.http_exception import HttpException
from arcana_server.settings import DEFAULT_LANGUAGE_CODE
from arcana_server.utils import get_body_in_request
from main.mappers import RequestToCategoriesMapper
from main.repositories import CategoryRepository, QuestionRepository, GameSessionRepository
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
        if 'uuid' not in request.query_params:
            raise HttpException('uuid field not provided', Errors.BAD_REQUEST)

        try:
            uuid_data = uuid.UUID(request.query_params['uuid']).hex
        except Exception as ex:
            raise HttpException('Wrong uuid format: %s' % str(ex), Errors.BAD_REQUEST)

        game_session = GameSessionRepository.get_session(uuid_data)

        language_code = request.META.get('HTTP_LANGUAGE', DEFAULT_LANGUAGE_CODE).lower()
        categories = RequestToCategoriesMapper.map(request.query_params)
        question, is_last = QuestionRepository.get_random_question(categories, game_session)
        return Response({
            'question': camelize(QuestionSerializer(question, context={'language_code': language_code}).data),
            'isLast': is_last
        }, status=200)
