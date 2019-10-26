from django.urls import path

from . import views

urlpatterns = [
    path('test', views.Test.as_view()),
    path('categories', views.Categories.as_view()),
    path('get_random_question', views.RandomQuestion.as_view()),
]