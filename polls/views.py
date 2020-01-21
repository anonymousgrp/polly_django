from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.

def index(request):
    questions = Question.objects.order_by('-pub_date')
    choices = Choice.objects.all()
    context = {
        'questions': questions,
        'choices': choices
    }
    return render(request, 'index.html', context)

def detail(request, question_id): 
    question = get_object_or_404(Question, pk = question_id)
    choices = question.choice_set.all()
    return render(request, 'detail.html', {'question': question, 'choices': choices})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
        print('Vote for ', choice.choice_text)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', { 'question': question, error_message: "You did't select a choice" })
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))
