from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Answer)


class QuestionInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


admin.site.register(Question, QuestionAdmin)
