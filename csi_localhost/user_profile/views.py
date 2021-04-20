from django.contrib.auth import logout as log_me_out
from django.shortcuts import render, redirect
from csi_localhost.rules.models import Rules
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def profile_view(request):
    user = request.user
    rules = Rules.objects.all().order_by('priority')
    if user.is_authenticated:
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return render(request, 'profile/start.html',{'rules':rules})
        elif request.method == "GET":
            try:
                profile = user.profile
                return render(request, 'profile/start.html',{'rules':rules})
            except Profile.DoesNotExist:
                form = ProfileForm(initial={'nick_name': user.username})
                return render(request, 'profile/profile.html', {'form': form})
    else:
        return redirect('home')


def leader_view(request):
    context = {'profiles': Profile.objects.all().order_by('-marks')}
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            if profile:
                if profile.current_question:
                    context['text'] = "Let's Continue"
                    context['has_started'] = True
                else:
                    context['text'] = "Let's Start"
                    context['has_started'] = False
        except Profile.DoesNotExist:
            context['text'] = "Let's Start"
            context['has_started'] = False
    else:
        context['text'] = "Let's Start"
        context['has_started'] = False
    return render(request, 'profile/lead.html', context)


def logout(request):
    log_me_out(request)
    return redirect('home')
