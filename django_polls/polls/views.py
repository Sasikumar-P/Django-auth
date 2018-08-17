from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Choice, Question

@login_required
def index(request):
    template_name = 'polls/index.html'
    questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, template_name, {'questions': questions})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def vote(request, question_id):
    print question_id
    print request.POST['choice']
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
