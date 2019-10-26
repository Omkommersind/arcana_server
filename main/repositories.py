from .models import Category, Question, Answer
from arcana_server.errors.errors import Errors
from arcana_server.errors.http_exception import HttpException


class CategoryRepository:

    @classmethod
    def get_all_categories(cls):
        return Category.objects.all()


class QuestionRepository:

    @classmethod
    def get_random_question(cls, categories):
        if categories is None:
            return Question.objects.order_by("?").first()
        return Question.objects.filter(category__in=categories).order_by("?").first()


class AnswerRepository:

    @classmethod
    def get_question_answers(cls, question: Question):
        return Answer.objects.filter(question=question)
