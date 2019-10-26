import uuid as uuid

from arcana_server.errors.exceptions import EntityDoesNotExistException
from .models import Category, Question, Answer, GameSession
from arcana_server.errors.errors import Errors
from arcana_server.errors.http_exception import HttpException


class CategoryRepository:

    @classmethod
    def get_all_categories(cls):
        return Category.objects.all()


class QuestionRepository:

    @classmethod
    def get_random_question(cls, categories, game_session: GameSession):
        if categories is None:
            # Deprecated
            return Question.objects.order_by("?").first()

        question = Question.objects.all().exclude(gamesession=game_session).order_by("?").first()
        if question is None:
            raise HttpException('No more questions', Errors.NOT_FOUND)

        cls.mark_asked_question(game_session, question)
        is_last = not Question.objects.all().exclude(gamesession=game_session).exists()

        return question, is_last

    @classmethod
    def mark_asked_question(cls, game_session: GameSession, question: Question):
        game_session.questions.add(question)
        game_session.save()
        return game_session


class AnswerRepository:

    @classmethod
    def get_question_answers(cls, question: Question):
        return Answer.objects.filter(question=question)


class GameSessionRepository:

    @classmethod
    def get_session(cls, uuid_data: uuid):
        try:
            return GameSession.objects.get(id=uuid_data)
        except GameSession.DoesNotExist:
            return GameSession.objects.create(id=uuid_data)
