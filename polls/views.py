from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.views import generic
from django.urls import reverse
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/auth')
    questions = Question.objects.order_by('-pub_date')
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'questions'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id): 
#     question = get_object_or_404(Question, pk = question_id)
#     choices = question.choice_set.all()
#     return render(request, 'detail.html', {'question': question, 'choices': choices})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'result.html', {'question': question})

# class ResultView(generic.DetailView):
#     models = Question
#     template_name = 'result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', { 'question': question, error_message: "You did't select a choice" })
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))
