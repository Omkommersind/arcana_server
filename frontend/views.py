from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.views import APIView


class GameView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/home.html')

    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


