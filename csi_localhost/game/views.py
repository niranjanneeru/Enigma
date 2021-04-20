import datetime

from django.shortcuts import render, get_object_or_404, redirect

from csi_localhost.response.models import Response
from .forms import AnswerForm
from .models import Question, Meme
from ..user_profile import models


# Create your views here.
def question_view(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except models.Profile.DoesNotExist:

            return redirect('user_profile:redirect')

        context = {'completed': False}
        if request.method == 'POST':
            form = AnswerForm(request.POST)

            if form.is_valid():
                answer = form.data.get('answer')
                response = Response(user=profile, question=profile.current_question, answer=answer,
                                    create_date=datetime.datetime.now())
                profile.last_submission = datetime.datetime.now()
                if answer and answer == profile.current_question.answer:
                    response.status = 1
                    response.save()
                    message = Meme.objects.filter(category=1).order_by('?').first()
                    context['result'] = dict(title=answer, message=message, indicator=1, color="green")
                    number = profile.current_question.number + 1
                    profile.marks = profile.marks + profile.current_question.marks

                    if number > len(Question.objects.all()):
                        profile.has_completed = True
                        profile.save()
                        context['completed'] = True
                        return render(request, 'game/result.html', context)

                    else:
                        profile.current_question = Question.objects.get(number=number)
                        profile.save()
                        return render(request, 'game/result.html', context)

                else:
                    response.status = 0
                    response.save()
                    profile.save()
                    message = Meme.objects.filter(category=2).order_by('?').first()
                    context['result'] = dict(title=answer, message=message, indicator=0, color="red")
                    return render(request, 'game/result.html', context)

            else:
                context['form'] = form
                return render(request, 'game/question.html', context)

        elif request.method == "GET":

            if profile.has_completed:
                message = Meme.objects.filter(category=4).order_by('?').first()
                return render(request, 'game/end.html', {"flag": 1, "message": message})

            if profile.current_question is None:
                queryset = get_object_or_404(Question, number=1)
                profile.current_question = queryset
                profile.save()

            if profile.current_question.is_active:
                context['question'] = profile.current_question
                context['form'] = AnswerForm()
                return render(request, 'game/question.html', context)
            else:
                message = Meme.objects.filter(category=3).order_by('?').first()
                return render(request, 'game/end.html', {"flag": 0, "message": message})
