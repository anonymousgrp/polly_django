from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
from django.views import generic
from django.urls import reverse
# Create your views here.


def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            error_message: "You did't select a choice"
        })
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))
