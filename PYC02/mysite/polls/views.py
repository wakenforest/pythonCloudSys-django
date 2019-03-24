from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s" % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "Your're looking at the results of questions %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s" % question_id)


