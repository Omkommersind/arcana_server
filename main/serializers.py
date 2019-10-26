from rest_framework import serializers

from localization_app.repositories import LocalizedStringRepository
from main.repositories import AnswerRepository
from .models import Category, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, category: Category):
        return LocalizedStringRepository.try_get_localized_string(category.name, self.context.get('language_code'))

    class Meta:
        model = Category
        fields = 'id', 'name'


class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    def get_text(self, answer: Answer):
        return LocalizedStringRepository.try_get_localized_string(answer.text, self.context.get('language_code'))

    class Meta:
        model = Answer
        fields = 'id', 'text'


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    def get_text(self, question: Question):
        return LocalizedStringRepository.try_get_localized_string(question.text, self.context.get('language_code'))

    def get_answers(self, question: Question):
        answers = AnswerRepository.get_question_answers(question)
        return AnswerSerializer(answers, context={'language_code': self.context.get('language_code')}, many=True).data

    class Meta:
        model = Question
        fields = 'id', 'text', 'category', 'answers', 'right_answer'

