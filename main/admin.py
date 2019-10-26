from django.contrib import admin
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(GameSession)
