from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from .models import Question


def index(request):
    question_list = Question.objects.all()
    output = ', '.join([str(a) for a in question_list])
    return HttpResponse(output)
