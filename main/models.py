import uuid

from django.db import models

from localization_app.models import DataString
from localization_app.repositories import LocalizedStringRepository


class Category(models.Model):
    name = models.ForeignKey(DataString, on_delete=models.CASCADE)

    def __str__(self):
        return 'ID: %d, %s' % (self.id, LocalizedStringRepository.get_default_localization(self.name))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    text = models.ForeignKey(DataString, on_delete=models.CASCADE)
    right_answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='right_answer', null=True,
                                     blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        if self.category:
            return 'ID: %d, (%s) - %s' % (self.id,
                                          LocalizedStringRepository.get_default_localization(self.category.name),
                                          LocalizedStringRepository.get_default_localization(self.text))
        return 'ID: %d - %s' % (self.id, LocalizedStringRepository.get_default_localization(self.text))

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Воспросы'


class Answer(models.Model):
    text = models.ForeignKey(DataString, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Answer ID: %d, %s' % (self.id, LocalizedStringRepository.get_default_localization(self.text))

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class GameSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    questions = models.ManyToManyField(Question, null=True, blank=True)

    def __str__(self):
        return '%s' % str(self.id)

    class Meta:
        verbose_name = 'Игровая сессия'
        verbose_name_plural = 'Игровые сессии'