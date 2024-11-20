import uuid
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView


class Index(CreateView):
    def get(self, request):
        user_id = request.session.session_key
        return HttpResponse(user_id)


class Detail(DetailView):
    pass